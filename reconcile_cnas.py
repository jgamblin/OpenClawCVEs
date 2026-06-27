#!/usr/bin/env python3
"""
reconcile_cnas.py — Scan the full CVE List V5 registry for every CVE affecting
OpenClaw, regardless of which CNA assigned it, and break the totals down by
assigner.

The main tracker (update_readme.py) is GHSA-anchored: it only discovers CVEs that
have an OpenClaw GitHub Security Advisory, so it sees ~50 project-issued CVEs and is
blind to the much larger stream of third-party assignments (the vast majority from
VulnCheck). This script closes that gap by scanning CVEProject/cvelistV5 directly.

Outputs (committed, read by update_readme.py / the dashboard):
    openclaw-cves-all.json   Reconciled full set, one row per CVE.
    cna-breakdown.json       Aggregates: by-assigner, project vs third-party, trend.

Usage:
    python3 reconcile_cnas.py            # Clone/refresh cvelistV5, scan, write JSON
    python3 reconcile_cnas.py --local    # Scan an existing .cvelistV5/ checkout only

Requirements:
    - Python 3.9+
    - git  — for the shallow sparse clone of cvelistV5
    - grep — fast candidate pre-filter over the large cves/ tree
"""

import json
import subprocess
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).parent
CVELIST_DIR = ROOT / ".cvelistV5"
CVELIST_REPO = "https://github.com/CVEProject/cvelistV5.git"

# Output files (flat JSON in repo root, matching cves.json / cve-pipeline-status.json)
ALL_CVES_FILE = ROOT / "openclaw-cves-all.json"
BREAKDOWN_FILE = ROOT / "cna-breakdown.json"

# Existing GHSA-pipeline data we cross-reference to mark which CVEs the old tracker
# already knew about. cves.json is the rendered summary; ghsa-advisories-full.json is
# the raw Advisory DB cache that survives the workflow's "clean generated files" step
# (which deletes cves.json before this script runs in CI), so we read both.
GHSA_CVES_FILE = ROOT / "cves.json"
GHSA_FULL_FILE = ROOT / "ghsa-advisories-full.json"

# Names the project has shipped under. Matches update_readme.py PACKAGES so the two
# data sources agree on what "OpenClaw" means.
MATCH_NAMES = {"openclaw", "clawdbot", "moltbot"}
REPO_REF = "github.com/openclaw/openclaw"

# Assigner short names that mean "the project issued this CVE itself" (GitHub as CNA
# for openclaw/openclaw security advisories).
PROJECT_ASSIGNERS = {"github_m"}

# Years of cvelistV5 to check out and scan. OpenClaw is a 2025/2026-era project; the
# current year is always included so the set stays correct over time.
_BASE_YEARS = ["2025", "2026"]


def _scan_years() -> list[str]:
    current = str(datetime.now(timezone.utc).year)
    years = list(_BASE_YEARS)
    if current not in years:
        years.append(current)
    return years


# ─── cvelistV5 checkout ──────────────────────────────────────────────────────


def ensure_cvelist(local_only: bool = False) -> bool:
    """Make sure .cvelistV5/ holds a sparse checkout of the cves/<year> trees.

    Uses a shallow, blobless, sparse clone so only the needed years are fetched
    (cves/ as a whole is multi-GB). Idempotent: an existing checkout is refreshed
    best-effort; on --local it is used as-is. Returns True if a usable checkout
    exists.
    """
    years = _scan_years()
    sparse_paths = [f"cves/{y}" for y in years]

    if local_only:
        if not CVELIST_DIR.exists():
            print(f"ERROR: --local but {CVELIST_DIR} does not exist.", file=sys.stderr)
            return False
        return True

    if CVELIST_DIR.exists():
        # Refresh in place (best-effort). Make sure the sparse set covers the
        # current year, then fast-forward.
        _run(["git", "-C", str(CVELIST_DIR), "sparse-checkout", "set", *sparse_paths],
             timeout=120)
        rc = _run(["git", "-C", str(CVELIST_DIR), "pull", "--depth", "1", "--ff-only"],
                  timeout=240)
        if rc != 0:
            print("WARNING: cvelistV5 refresh failed — scanning existing checkout.",
                  file=sys.stderr)
        return True

    print(f"Cloning cvelistV5 (shallow, blobless, sparse) into {CVELIST_DIR}...")
    rc = _run([
        "git", "clone", "--depth", "1", "--filter=blob:none", "--sparse",
        CVELIST_REPO, str(CVELIST_DIR),
    ], timeout=300)
    if rc != 0:
        print("ERROR: cvelistV5 clone failed.", file=sys.stderr)
        return False
    rc = _run(["git", "-C", str(CVELIST_DIR), "sparse-checkout", "set", *sparse_paths],
              timeout=240)
    if rc != 0:
        print("ERROR: sparse-checkout set failed.", file=sys.stderr)
        return False
    return True


def _run(cmd: list[str], timeout: int) -> int:
    """Run a subprocess with a hard wall-clock timeout; return its exit code.

    Returns a non-zero sentinel on timeout/failure so callers can fall back.
    """
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
        return result.returncode
    except (subprocess.TimeoutExpired, FileNotFoundError, Exception):
        return 1


def find_candidate_files() -> list[Path]:
    """Pre-filter the large cves/ tree to records that mention an OpenClaw name.

    grep over the checked-out year dirs is far cheaper than json-parsing every
    file. Returns absolute paths to candidate records.
    """
    dirs = [str(CVELIST_DIR / "cves" / y) for y in _scan_years()
            if (CVELIST_DIR / "cves" / y).exists()]
    if not dirs:
        return []
    pattern = "|".join(sorted(MATCH_NAMES))
    try:
        result = subprocess.run(
            ["grep", "-rliE", pattern, *dirs],
            capture_output=True, text=True, timeout=120,
        )
    except (subprocess.TimeoutExpired, FileNotFoundError, Exception):
        return []
    # grep exit code 1 == no matches (not an error); >1 == real error.
    if result.returncode > 1:
        return []
    return [Path(line) for line in result.stdout.splitlines() if line.strip()]


# ─── Matching & parsing (pure, unit-tested) ──────────────────────────────────


def match_openclaw(record: dict) -> bool:
    """True if a CVE record's affected products identify OpenClaw.

    Matches when any containers.cna.affected[] has vendor or product equal to one
    of the known project names (case-insensitive, trimmed), or references the
    openclaw/openclaw repo via collectionURL / packageName / repo.
    """
    affected = (record.get("containers", {}).get("cna", {}).get("affected") or [])
    for a in affected:
        if not isinstance(a, dict):
            continue
        for field in ("vendor", "product"):
            val = (a.get(field) or "").strip().lower()
            if val in MATCH_NAMES:
                return True
        for field in ("collectionURL", "packageName", "repo"):
            val = (a.get(field) or "").lower()
            if REPO_REF in val:
                return True
    return False


def summarize_record(record: dict) -> dict | None:
    """Extract the reconciled row for one CVE record.

    Returns None for REJECTED records (excluded by design).
    """
    meta = record.get("cveMetadata", {})
    state = (meta.get("state") or "").strip()
    if state.upper() == "REJECTED":
        return None
    return {
        "cve_id": meta.get("cveId", ""),
        "assigner": meta.get("assignerShortName", "") or "unknown",
        "date_published": (meta.get("datePublished", "") or "")[:10],
        "state": state or "UNKNOWN",
        "source": "cvelistV5",
    }


def aggregate(records: list[dict], ghsa_cve_ids: set[str]) -> dict:
    """Build the by-assigner / project-vs-third-party / monthly aggregates.

    Mutates each record to add in_ghsa_pipeline (whether the old GHSA-anchored
    tracker already covered it) and source ("cvelistV5+ghsa" when also in GHSA).
    """
    by_assigner = Counter()
    monthly = Counter()
    project_issued = 0
    third_party_issued = 0

    for r in records:
        assigner = r.get("assigner", "unknown")
        by_assigner[assigner] += 1
        if assigner.strip().lower() in PROJECT_ASSIGNERS:
            project_issued += 1
        else:
            third_party_issued += 1

        in_ghsa = r.get("cve_id") in ghsa_cve_ids
        r["in_ghsa_pipeline"] = in_ghsa
        if in_ghsa:
            r["source"] = "cvelistV5+ghsa"

        dp = r.get("date_published", "")
        if dp.startswith("2026") and len(dp) >= 7:
            monthly[dp[:7]] += 1

    total = len(records)
    by_assigner_list = [
        {
            "cna": cna,
            "count": count,
            "pct": round(count / total * 100, 1) if total else 0.0,
        }
        for cna, count in sorted(by_assigner.items(), key=lambda kv: (-kv[1], kv[0]))
    ]
    monthly_list = [{"month": m, "count": monthly[m]} for m in sorted(monthly)]

    return {
        "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC"),
        "total": total,
        "project_issued": project_issued,
        "third_party_issued": third_party_issued,
        "by_assigner": by_assigner_list,
        "monthly_2026": monthly_list,
    }


# ─── GHSA cross-reference ────────────────────────────────────────────────────


def load_ghsa_cve_ids() -> set[str]:
    """CVE IDs the existing GHSA-anchored pipeline already tracks.

    Unions the rendered summary (cves.json) with the raw Advisory DB cache
    (ghsa-advisories-full.json) so the cross-reference works both locally and in
    CI, where cves.json is removed before this script runs.
    """
    ids = set()
    for path in (GHSA_CVES_FILE, GHSA_FULL_FILE):
        if not path.exists():
            continue
        try:
            with open(path) as f:
                data = json.load(f)
        except (json.JSONDecodeError, OSError):
            continue
        for entry in data:
            if isinstance(entry, dict):
                cid = entry.get("cve_id")
                if cid:
                    ids.add(cid)
    return ids


# ─── Main ────────────────────────────────────────────────────────────────────


def collect(local_only: bool = False) -> tuple[list[dict], dict]:
    """Scan cvelistV5 and return (reconciled rows, aggregate breakdown)."""
    if not ensure_cvelist(local_only=local_only):
        sys.exit(1)

    candidates = find_candidate_files()
    print(f"Scanning {len(candidates)} candidate records...")

    records = []
    seen = set()
    for path in candidates:
        try:
            with open(path) as f:
                record = json.load(f)
        except (json.JSONDecodeError, OSError):
            continue
        if not match_openclaw(record):
            continue
        row = summarize_record(record)
        if row is None or not row["cve_id"] or row["cve_id"] in seen:
            continue
        seen.add(row["cve_id"])
        records.append(row)

    records.sort(key=lambda r: r["cve_id"])
    breakdown = aggregate(records, load_ghsa_cve_ids())
    return records, breakdown


def main():
    local_only = "--local" in sys.argv

    print("=" * 60)
    print("OpenClaw CVE List V5 — full CNA reconciliation")
    print("=" * 60)

    records, breakdown = collect(local_only=local_only)

    with open(ALL_CVES_FILE, "w") as f:
        json.dump(records, f, indent=2)
        f.write("\n")
    with open(BREAKDOWN_FILE, "w") as f:
        json.dump(breakdown, f, indent=2)
        f.write("\n")

    print(f"\n✅ {len(records)} OpenClaw CVEs written to {ALL_CVES_FILE.name}")
    print(f"   project-issued (GitHub): {breakdown['project_issued']}  ·  "
          f"third-party: {breakdown['third_party_issued']}")
    print("   Top assigners:")
    for entry in breakdown["by_assigner"][:5]:
        print(f"     {entry['count']:5d}  {entry['cna']} ({entry['pct']}%)")


if __name__ == "__main__":
    main()
