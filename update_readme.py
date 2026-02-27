#!/usr/bin/env python3
"""
update_readme.py — Fetch OpenClaw CVE/GHSA data and render README.md from a Jinja2 template.

Usage:
    python3 update_readme.py              # Full update (fetch + render)
    python3 update_readme.py --local      # Render from cached JSON files only (no API calls)

Requirements:
    - Python 3.9+
    - jinja2 (pip install jinja2)
    - gh CLI (authenticated) — for GitHub API calls
    - curl — for CVE Services API
"""

import base64
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

try:
    from jinja2 import Environment, FileSystemLoader
except ImportError:
    print("ERROR: jinja2 not installed. Run: pip install jinja2", file=sys.stderr)
    sys.exit(1)

ROOT = Path(__file__).parent
TEMPLATES_DIR = ROOT / "templates"
DATA_DIR = ROOT
CVE_RECORDS_DIR = ROOT / "cve-records"

# Project search terms
PACKAGES = ["openclaw", "clawdbot", "moltbot"]
CVELIST_SEARCH_TERMS = ["openclaw", "clawdbot", "moltbot", "clawhub"]


def run_gh(args: list[str], fallback=None):
    """Run a gh CLI command and return parsed JSON."""
    try:
        result = subprocess.run(
            ["gh", "api"] + args,
            capture_output=True, text=True, timeout=30
        )
        if result.returncode != 0:
            if fallback is not None:
                return fallback
            return None
        return json.loads(result.stdout) if result.stdout.strip() else None
    except (subprocess.TimeoutExpired, json.JSONDecodeError, FileNotFoundError):
        return fallback


def run_curl_json(url: str, fallback=None):
    """Run curl and return parsed JSON."""
    try:
        result = subprocess.run(
            ["curl", "-s", url],
            capture_output=True, text=True, timeout=15
        )
        if result.returncode != 0:
            return fallback
        return json.loads(result.stdout)
    except (subprocess.TimeoutExpired, json.JSONDecodeError, FileNotFoundError):
        return fallback


# ─── Data Fetching ───────────────────────────────────────────────────────────


def fetch_ghsas() -> list[dict]:
    """Fetch all GHSAs from the GitHub Advisory Database for our packages."""
    all_advisories = []
    seen_ids = set()

    for pkg in PACKAGES:
        page = 1
        while True:
            data = run_gh(
                [f"/advisories?affects={pkg}&per_page=100&page={page}"],
                fallback=[]
            )
            if not data:
                break
            for adv in data:
                ghsa_id = adv.get("ghsa_id", "")
                if ghsa_id not in seen_ids:
                    seen_ids.add(ghsa_id)
                    all_advisories.append(adv)
            if len(data) < 100:
                break
            page += 1

    return all_advisories


def fetch_repo_advisories() -> list[dict]:
    """Fetch all published security advisories directly from the openclaw/openclaw repo.

    This catches advisories that haven't been indexed in the global Advisory
    Database yet (repo-only GHSAs).  Requires the `gh` CLI with sufficient
    permissions (public-repo read is enough for published advisories).
    """
    all_advisories = []
    seen_ids = set()
    page = 1

    while True:
        data = run_gh(
            [f"/repos/openclaw/openclaw/security-advisories?per_page=100&state=published&page={page}"],
            fallback=[]
        )
        if not data:
            break
        for adv in data:
            ghsa_id = adv.get("ghsa_id", "")
            if ghsa_id and ghsa_id not in seen_ids:
                seen_ids.add(ghsa_id)
                all_advisories.append(adv)
        if len(data) < 100:
            break
        page += 1

    return all_advisories


def parse_repo_advisory_summary(adv: dict) -> dict:
    """Extract a lightweight summary from a repo-level advisory."""
    return {
        "ghsa_id": adv.get("ghsa_id", ""),
        "severity": (adv.get("severity", "unknown") or "unknown").upper(),
        "title": (adv.get("summary", "") or "").replace("\n", " ").strip(),
        "html_url": adv.get("html_url", "") or f"https://github.com/openclaw/openclaw/security/advisories/{adv.get('ghsa_id', '')}",
    }


def fetch_cvelist_cves() -> list[str]:
    """Search cvelistV5 for OpenClaw CVEs via GitHub code search.

    Returns a list of CVE ID strings (e.g. ["CVE-2025-12345", ...]).
    """
    cve_files = {}

    for term in CVELIST_SEARCH_TERMS:
        data = run_gh(
            ["search/code", "-q",
             f"q={term}+repo:CVEProject/cvelistV5+path:cves/&per_page=100"],
            fallback={"items": []}
        )
        for item in (data or {}).get("items", []):
            name = item.get("name", "")
            if name.startswith("CVE-") and name.endswith(".json"):
                cve_id = name.replace(".json", "")
                if cve_id not in cve_files:
                    cve_files[cve_id] = item.get("path", "")

    return list(cve_files.keys())


def fetch_cve_record(cve_id: str) -> dict | None:
    """Fetch a CVE record from cvelistV5."""
    year = cve_id.split("-")[1]
    num = cve_id.split("-")[2]
    prefix = num[:2] + "xxx"
    path = f"cves/{year}/{prefix}/{cve_id}.json"

    data = run_gh(
        [f"repos/CVEProject/cvelistV5/contents/{path}",
         "--jq", ".download_url"],
        fallback=None
    )
    if data and isinstance(data, str):
        return run_curl_json(data.strip())

    # Try raw content approach
    content_data = run_gh(
        [f"repos/CVEProject/cvelistV5/contents/{path}"],
        fallback=None
    )
    if content_data and "content" in content_data:
        try:
            decoded = base64.b64decode(content_data["content"])
            return json.loads(decoded)
        except Exception:
            pass
    return None


def check_cve_state(cve_id: str) -> str:
    """Check CVE state via CVE Services API."""
    data = run_curl_json(f"https://cveawg.mitre.org/api/cve-id/{cve_id}")
    if data and "state" in data:
        return data["state"]
    return "UNKNOWN"


def check_cvelist_exists(cve_id: str) -> bool:
    """Check if a CVE record exists in cvelistV5."""
    year = cve_id.split("-")[1]
    num = cve_id.split("-")[2]
    prefix = num[:2] + "xxx"
    path = f"cves/{year}/{prefix}/{cve_id}.json"

    try:
        result = subprocess.run(
            ["gh", "api", f"repos/CVEProject/cvelistV5/contents/{path}",
             "-i", "--silent"],
            capture_output=True, text=True, timeout=15
        )
        first_line = result.stdout.split("\n")[0] if result.stdout else ""
        return "200" in first_line
    except (subprocess.TimeoutExpired, FileNotFoundError):
        return False


# ─── Data Parsing ────────────────────────────────────────────────────────────


def parse_ghsa_summary(adv: dict) -> dict:
    """Extract key fields from a raw GHSA advisory."""
    vulns = adv.get("vulnerabilities", [])
    fixed_versions = [
        v.get("first_patched_version")
        for v in vulns
        if v.get("first_patched_version")
    ]
    fixed_versions_unique = []
    for v in fixed_versions:
        if v and v not in fixed_versions_unique:
            fixed_versions_unique.append(v)

    return {
        "ghsa_id": adv.get("ghsa_id", ""),
        "cve_id": adv.get("cve_id"),
        "severity": adv.get("severity", "unknown"),
        "title": (adv.get("summary", "") or "").replace("\n", " ").strip(),
        "published": (adv.get("published_at", "") or "")[:10],
        "html_url": adv.get("html_url", ""),
        "packages": [
            f"{v['package']['ecosystem']}/{v['package']['name']}"
            for v in vulns if v.get("package")
        ],
        "affected_versions": [
            v.get("vulnerable_version_range", "")
            for v in vulns
        ],
        "fixed_versions": fixed_versions_unique,
        "fixed_version": ", ".join(fixed_versions_unique) if fixed_versions_unique else "",
        "cwes": [
            c.get("cwe_id", "") for c in adv.get("cwes", [])
        ],
    }


def parse_cve_record(record: dict) -> dict:
    """Extract key fields from a raw CVE JSON 5.x record."""
    meta = record.get("cveMetadata", {})
    cna = record.get("containers", {}).get("cna", {})
    adp_list = record.get("containers", {}).get("adp", [])

    # Basic fields
    cve_id = meta.get("cveId", "")
    state = meta.get("state", "")
    date_published = (meta.get("datePublished", "") or "")[:10]
    assigner = meta.get("assignerShortName", "")

    # Title & description
    title = cna.get("title", "") or ""
    descriptions = cna.get("descriptions", [])
    description = ""
    for d in descriptions:
        if d.get("lang", "").startswith("en"):
            description = d.get("value", "")
            break
    if not description and descriptions:
        description = descriptions[0].get("value", "")

    # Metrics
    cvss_score = None
    cvss_severity = ""
    vector_string = ""
    for metric_block in cna.get("metrics", []):
        for key in ["cvssV4_0", "cvssV3_1", "cvssV3_0", "cvssV2_0"]:
            if key in metric_block:
                m = metric_block[key]
                cvss_score = m.get("baseScore")
                cvss_severity = m.get("baseSeverity", "").upper()
                vector_string = m.get("vectorString", "")
                break
        if cvss_score:
            break

    # CWEs
    cwes = []
    for p in cna.get("problemTypes", []):
        for desc in p.get("descriptions", []):
            cwe_id = desc.get("cweId", "")
            cwe_desc = desc.get("description", "")
            if cwe_id:
                cwes.append({"id": cwe_id, "description": cwe_desc})

    # Affected products
    affected = cna.get("affected", [])
    vendor = ""
    product = ""
    purl = ""
    affected_versions = ""
    for a in affected:
        vendor = a.get("vendor", vendor)
        product = a.get("product", product)
        purl = a.get("packageURL", purl) if not purl else purl
        for v in a.get("versions", []):
            if v.get("status") == "affected":
                lt = v.get("lessThan", v.get("version", "?"))
                if lt.startswith("<"):
                    affected_versions = lt.strip()
                else:
                    affected_versions = f"< {lt}"

    # References
    references = []
    advisory_url = ""
    for ref in cna.get("references", []):
        url = ref.get("url", "")
        tags = ref.get("tags", [])
        name = ref.get("name", "") or url.split("/")[-1]
        if "x_refsource_CONFIRM" in tags or "vendor-advisory" in tags or "github.com" in url and "advisories" in url:
            advisory_url = url
        references.append({"url": url, "name": name, "tags": tags})

    # GHSA ID from advisory URL
    ghsa_id = ""
    if advisory_url:
        parts = advisory_url.rstrip("/").split("/")
        if parts and parts[-1].startswith("GHSA-"):
            ghsa_id = parts[-1]

    # CISA SSVC (from ADP containers)
    cisa_ssvc = ""
    for adp in adp_list:
        if adp.get("providerMetadata", {}).get("shortName", "").upper() == "CISA-ADP":
            for metric in adp.get("metrics", []):
                other = metric.get("other", {})
                if other.get("type") == "ssvc":
                    content = other.get("content", {})
                    options = content.get("options", {})
                    parts = []
                    if "Exploitation" in options:
                        parts.append(f"Exploitation: {options['Exploitation']}")
                    if "Automatable" in options:
                        parts.append(f"Automatable: {options['Automatable']}")
                    if "Technical Impact" in options or "Technical_Impact" in content:
                        ti = options.get("Technical Impact", content.get("Technical_Impact", ""))
                        parts.append(f"Technical Impact: {ti}")
                    cisa_ssvc = " · ".join(parts)

    # Naming notes
    naming_note = ""
    desc_names = "OpenClaw"
    if "clawdbot" in vendor.lower() or "clawdbot" in product.lower():
        naming_note = f"Uses old name `{vendor}/{product}` as vendor/product."
        desc_names = "OpenClaw (formerly Clawdbot)"
    elif "moltbot" in description.lower() or "clawdbot" in description.lower():
        all_names = []
        for name in ["OpenClaw", "clawdbot", "Moltbot"]:
            if name.lower() in description.lower():
                all_names.append(name)
        desc_names = " / ".join(all_names) if all_names else "OpenClaw"
        if purl and "clawdbot" in purl:
            naming_note = f"Uses all three names in description. packageURL still references `{purl}`."
        elif len(all_names) > 1:
            naming_note = f"References multiple names: {', '.join(all_names)}."

    # Fallback title: use a shorter extraction from description
    if not title and description:
        # Take up to the first period or 80 chars, whichever is shorter
        first_sentence = description.split(". ")[0] if ". " in description else description[:80]
        # If the sentence is too generic, try to extract the key action
        if len(first_sentence) > 80:
            first_sentence = first_sentence[:80].rsplit(" ", 1)[0] + "\u2026"
        title = first_sentence

    return {
        "cve_id": cve_id,
        "state": state,
        "date_published": date_published,
        "assigner": assigner,
        "title": title,
        "description": description,
        "cvss": cvss_score,
        "severity": cvss_severity,
        "vector_string": vector_string,
        "cwes": ", ".join(c["id"] for c in cwes),
        "cwes_long": ", ".join(f"{c['id']} ({c['description']})" for c in cwes),
        "vendor": vendor,
        "product": product,
        "purl": purl or None,
        "affected_versions": affected_versions,
        "advisory_url": advisory_url,
        "ghsa_id": ghsa_id,
        "references": [r for r in references if "github.com" not in r["url"] or "advisories" not in r["url"]],
        "cisa_ssvc": cisa_ssvc,
        "naming_note": naming_note,
        "desc_names": desc_names,
    }


# ─── Repo-Only Advisories ───────────────────────────────────────────────────

# These are advisories visible on the repo security page but not indexed in the
# GitHub Advisory Database. They are now auto-refreshed from the repo security
# advisories API during each update, but we keep the JSON file as a cache for
# --local runs.

REPO_ONLY_GHSAS_FILE = ROOT / "repo-only-ghsas.json"

SEVERITY_BADGES = {
    "critical": "![Critical](https://img.shields.io/badge/CRITICAL-8b0000?style=flat-square)",
    "high": "![High](https://img.shields.io/badge/HIGH-d63031?style=flat-square)",
    "medium": "![Medium](https://img.shields.io/badge/MEDIUM-e17055?style=flat-square)",
    "moderate": "![Medium](https://img.shields.io/badge/MODERATE-e17055?style=flat-square)",
    "low": "![Low](https://img.shields.io/badge/LOW-fdcb6e?style=flat-square)",
}


def severity_badge(severity: str) -> str:
    """Return a Shields.io badge for a severity level."""
    return SEVERITY_BADGES.get(severity.lower(), severity.upper())


def load_repo_only_ghsas() -> list[dict]:
    """Load repo-only GHSAs from the external JSON file."""
    if REPO_ONLY_GHSAS_FILE.exists():
        with open(REPO_ONLY_GHSAS_FILE) as f:
            return json.load(f)
    print(f"WARNING: {REPO_ONLY_GHSAS_FILE} not found, using empty list", file=sys.stderr)
    return []


# ─── Main Logic ──────────────────────────────────────────────────────────────


def collect_data(local_only: bool = False) -> dict:
    """Collect all data needed to render the README."""

    # ── GHSAs from Advisory DB ──
    if local_only and (DATA_DIR / "ghsa-advisories-full.json").exists():
        print("Loading cached GHSA data...")
        with open(DATA_DIR / "ghsa-advisories-full.json") as f:
            raw_ghsas = json.load(f)
    else:
        print("Fetching GHSAs from GitHub Advisory Database...")
        raw_ghsas = fetch_ghsas()
        with open(DATA_DIR / "ghsa-advisories-full.json", "w") as f:
            json.dump(raw_ghsas, f, indent=2)

    ghsas = [parse_ghsa_summary(a) for a in raw_ghsas]
    ghsas.sort(key=lambda x: x["published"], reverse=True)

    # Save summary
    with open(DATA_DIR / "ghsa-advisories.json", "w") as f:
        json.dump(ghsas, f, indent=2)

    advisory_db_ids = set(g["ghsa_id"] for g in ghsas)

    # ── Repo-only GHSAs (auto-refresh or cached) ──
    repo_cve_ids = set()  # CVE IDs discovered from repo advisory API
    if local_only:
        repo_only_ghsas = load_repo_only_ghsas()
    else:
        print("Fetching repo-level security advisories...")
        raw_repo = fetch_repo_advisories()
        print(f"  Found {len(raw_repo)} repo advisories")
        # Capture any CVE IDs assigned via repo advisories that may not be in
        # the global advisory DB yet.
        for adv in raw_repo:
            cve_id = adv.get("cve_id")
            if cve_id:
                repo_cve_ids.add(cve_id)
        # Keep only those NOT already in the Advisory DB (deduplicate)
        repo_only_ghsas = []
        for adv in raw_repo:
            ghsa_id = adv.get("ghsa_id", "")
            if ghsa_id and ghsa_id not in advisory_db_ids:
                repo_only_ghsas.append(parse_repo_advisory_summary(adv))
        severity_order = {"CRITICAL": 0, "HIGH": 1, "MODERATE": 2, "MEDIUM": 2, "LOW": 3}
        repo_only_ghsas.sort(key=lambda x: (severity_order.get(x["severity"], 4), x["ghsa_id"]))
        print(f"  Repo-only (not in advisory DB): {len(repo_only_ghsas)}")
        # Persist for --local runs
        with open(REPO_ONLY_GHSAS_FILE, "w") as f:
            json.dump(repo_only_ghsas, f, indent=2)
            f.write("\n")

    # ── Split GHSAs ──
    ghsas_with_cve = [g for g in ghsas if g["cve_id"]]
    ghsas_no_cve = [g for g in ghsas if not g["cve_id"]]

    # Collect CVE IDs from both advisory DB and repo-level advisories
    all_cve_ids_set = set(g["cve_id"] for g in ghsas_with_cve)
    # Also include CVE IDs discovered via the repo advisory API that may not
    # have appeared in the global advisory DB yet.
    all_cve_ids_set |= repo_cve_ids
    all_cve_ids = sorted(all_cve_ids_set)

    # ── CVE Records from cvelistV5 ──
    published_cves = []
    cvelist_cve_ids = set()

    if local_only:
        # Load from cached cve-records/
        for f in sorted(CVE_RECORDS_DIR.glob("CVE-*.json")):
            with open(f) as fh:
                record = json.load(fh)
            parsed = parse_cve_record(record)
            published_cves.append(parsed)
            cvelist_cve_ids.add(parsed["cve_id"])
    else:
        print("Searching cvelistV5 for OpenClaw CVEs...")
        found_cve_ids = fetch_cvelist_cves()

        # Also check all GHSA CVE IDs
        for cve_id in all_cve_ids:
            if cve_id not in found_cve_ids:
                found_cve_ids.append(cve_id)

        print(f"Checking {len(found_cve_ids)} CVE IDs against cvelistV5...")
        CVE_RECORDS_DIR.mkdir(exist_ok=True)

        for cve_id in sorted(found_cve_ids):
            exists = check_cvelist_exists(cve_id)
            if exists:
                cvelist_cve_ids.add(cve_id)
                # Try to load cached record first
                cached = CVE_RECORDS_DIR / f"{cve_id}.json"
                if cached.exists():
                    with open(cached) as fh:
                        record = json.load(fh)
                else:
                    print(f"  Fetching {cve_id} from cvelistV5...")
                    record = fetch_cve_record(cve_id)
                    if record:
                        with open(cached, "w") as fh:
                            json.dump(record, fh, indent=2)

                if record:
                    published_cves.append(parse_cve_record(record))

    published_cves.sort(key=lambda x: x.get("cvss") or 0, reverse=True)

    # Patch in fixed versions from GHSA data (first_patched_version)
    ghsa_fixed_by_id = {g.get("ghsa_id"): g.get("fixed_version", "") for g in ghsas if g.get("ghsa_id")}
    ghsa_fixed_by_cve = {g.get("cve_id"): g.get("fixed_version", "") for g in ghsas_with_cve if g.get("cve_id")}
    for cve in published_cves:
        fixed = ""
        if cve.get("ghsa_id"):
            fixed = ghsa_fixed_by_id.get(cve["ghsa_id"], "")
        if not fixed and cve.get("cve_id"):
            fixed = ghsa_fixed_by_cve.get(cve["cve_id"], "")
        cve["fixed_version"] = fixed

    # Patch in GHSA titles for CVEs with missing/poor titles
    ghsa_title_map = {g["cve_id"]: g["title"] for g in ghsas_with_cve if g.get("cve_id")}
    for cve in published_cves:
        ghsa_title = ghsa_title_map.get(cve["cve_id"], "")
        if ghsa_title and (not cve["title"] or len(cve["title"]) > 80 or cve["title"].startswith("OpenClaw (aka")):
            cve["title"] = ghsa_title

    # Save published CVE summaries (after title patching)
    with open(DATA_DIR / "cves.json", "w") as f:
        json.dump(
            [{"cve_id": c["cve_id"], "severity": c["severity"], "cvss": c["cvss"],
              "title": c["title"], "date_published": c["date_published"],
              "ghsa_id": c["ghsa_id"]}
             for c in published_cves],
            f, indent=2
        )

    # ── Pipeline Status (CVE state for all GHSA CVE IDs) ──
    pipeline = []
    cves_published_count = 0
    cves_reserved_count = 0

    for cve_id in sorted(all_cve_ids):
        in_cvelist = cve_id in cvelist_cve_ids

        if local_only:
            state = "PUBLISHED" if in_cvelist else "RESERVED"
        else:
            state = check_cve_state(cve_id)

        ghsa_pub = ""
        cna = ""
        for g in ghsas_with_cve:
            if g["cve_id"] == cve_id:
                ghsa_pub = g["published"]
                break
        for c in published_cves:
            if c["cve_id"] == cve_id:
                cna = c.get("assigner", "")
                break

        if state == "PUBLISHED":
            cves_published_count += 1
        else:
            cves_reserved_count += 1

        pipeline.append({
            "cve_id": cve_id,
            "state": state,
            "in_cvelist": in_cvelist,
            "ghsa_published": ghsa_pub,
            "cna": cna,
        })

    # Save pipeline status
    with open(DATA_DIR / "cve-pipeline-status.json", "w") as f:
        json.dump({
            "analysis_date": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
            "published": [p for p in pipeline if p["state"] == "PUBLISHED"],
            "reserved": [p for p in pipeline if p["state"] != "PUBLISHED"],
        }, f, indent=2)

    # ── Severity Counts (deduplicated) ──
    # repo_only_ghsas is already guaranteed not to overlap with ghsas (advisory DB),
    # so a simple concatenation is safe here.
    all_severities = [g["severity"].lower() for g in ghsas] + [
        r["severity"].lower() for r in repo_only_ghsas
    ]
    severity_critical = sum(1 for s in all_severities if s == "critical")
    severity_high = sum(1 for s in all_severities if s == "high")
    severity_medium = sum(1 for s in all_severities if s in ("medium", "moderate"))
    severity_low = sum(1 for s in all_severities if s == "low")

    # ── Naming Issues ──
    naming_issues = []
    for cve in published_cves:
        naming_issues.append({
            "cve_id": cve["cve_id"],
            "vendor": cve["vendor"],
            "product": cve["product"],
            "purl": f"`{cve['purl']}`" if cve.get("purl") else None,
            "desc_names": cve["desc_names"],
        })

    # ── Vulnerability Categories ──
    vuln_categories = [
        {"name": "OS Command Injection (CWE-78)", "count": 0, "examples": "PATH injection, SSH command injection, Docker exec, keychain writes"},
        {"name": "Path Traversal (CWE-22)", "count": 0, "examples": "MEDIA: paths, plugin install, browser downloads, Zip Slip, transcript paths"},
        {"name": "SSRF", "count": 0, "examples": "Image tool fetch, Feishu extension, attachment/media URLs, IPv6 bypass"},
        {"name": "Auth Bypass / Missing Auth", "count": 0, "examples": "WebSocket config.apply, webhook verification, browser relay, sandbox bridge"},
        {"name": "Allowlist Bypass", "count": 0, "examples": "Telegram usernames, Matrix displayName, Slack DM, Twitch, voice-call"},
        {"name": "Injection (XSS/CSRF/Prompt)", "count": 0, "examples": "XSS in Control UI, prompt injection via Slack/CWD/logs, CSRF"},
        {"name": "Denial of Service", "count": 0, "examples": "Unbounded media fetch, webhook body buffering, archive expansion"},
    ]

    # Count categories from all advisory titles (deduplicated)
    all_titles = [g["title"].lower() for g in ghsas] + [r["title"].lower() for r in repo_only_ghsas]
    for title in all_titles:
        if any(w in title for w in ["command injection", "command hijack", "rce", "code execution", "shell injection"]):
            vuln_categories[0]["count"] += 1
        if any(w in title for w in ["path traversal", "zip slip", "lfi", "local file", "file read", "file write", "file disclosure"]):
            vuln_categories[1]["count"] += 1
        if "ssrf" in title:
            vuln_categories[2]["count"] += 1
        if any(w in title for w in ["auth bypass", "missing auth", "authentication", "missing webhook", "unauthenticated"]):
            vuln_categories[3]["count"] += 1
        if any(w in title for w in ["allowlist", "bypass", "allowfrom"]):
            vuln_categories[4]["count"] += 1
        if any(w in title for w in ["xss", "csrf", "injection", "prompt", "spoofing"]):
            vuln_categories[5]["count"] += 1
        if any(w in title for w in ["dos", "unbounded", "denial"]):
            vuln_categories[6]["count"] += 1

    total_ghsas = len(ghsas) + len(repo_only_ghsas)

    # ── Add severity badges to all records ──
    for cve in published_cves:
        cve["severity_badge"] = severity_badge(cve.get("severity", ""))

    all_ghsas_combined = ghsas_with_cve + ghsas_no_cve
    for g in all_ghsas_combined:
        g["severity_badge"] = severity_badge(g.get("severity", ""))
    for g in repo_only_ghsas:
        g["severity_badge"] = severity_badge(g.get("severity", ""))

    # ── Severity-grouped advisory lists ──
    all_ghsas_sorted = sorted(all_ghsas_combined, key=lambda x: x["published"], reverse=True)
    ghsas_critical_high = [g for g in all_ghsas_sorted if g["severity"].lower() in ("critical", "high")]
    ghsas_medium = [g for g in all_ghsas_sorted if g["severity"].lower() in ("medium", "moderate")]
    ghsas_low = [g for g in all_ghsas_sorted if g["severity"].lower() == "low"]

    # ── Insights ──
    categorized_total = sum(c["count"] for c in vuln_categories)
    top_cwe = None
    if categorized_total > 0:
        top_cat = max(vuln_categories, key=lambda c: c["count"])
        top_cwe = {
            "name": top_cat["name"],
            "count": top_cat["count"],
            "total": categorized_total,
            "pct": round(top_cat["count"] / categorized_total * 100),
        }

    sync_rate_pct = round(cves_published_count / len(all_cve_ids) * 100) if all_cve_ids else 0

    # Date range of advisories
    all_dates = [g["published"] for g in ghsas if g.get("published")]
    if all_dates:
        earliest = min(all_dates)[:10]
        latest = max(all_dates)[:10]
        advisory_date_range = f"{earliest} → {latest}"
    else:
        advisory_date_range = "N/A"

    high_impact_pct = round((severity_critical + severity_high) / total_ghsas * 100) if total_ghsas else 0

    return {
        "updated_at": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC"),
        "counts": {
            "total_ghsas": total_ghsas,
            "total_cves": len(all_cve_ids),
            "cves_published": cves_published_count,
            "cves_reserved": cves_reserved_count,
            "ghsas_no_cve": total_ghsas - len(all_cve_ids),
            "ghsas_indexed_no_cve": len(ghsas_no_cve),
            "severity_critical": severity_critical,
            "severity_high": severity_high,
            "severity_medium": severity_medium,
            "severity_low": severity_low,
            "repo_only": len(repo_only_ghsas),
        },
        "published_cves": published_cves,
        "pipeline_status": pipeline,
        "ghsas_with_cve": sorted(ghsas_with_cve, key=lambda x: x["published"], reverse=True),
        "ghsas_no_cve": sorted(ghsas_no_cve, key=lambda x: (
            {"critical": 0, "high": 1, "medium": 2, "moderate": 2, "low": 3}.get(x["severity"].lower(), 4),
            x["published"]
        )),
        "ghsas_critical_high": ghsas_critical_high,
        "ghsas_medium": ghsas_medium,
        "ghsas_low": ghsas_low,
        "repo_only_ghsas": repo_only_ghsas,
        "naming_issues": naming_issues,
        "vuln_categories": vuln_categories,
        "top_cwe": top_cwe,
        "sync_rate_pct": sync_rate_pct,
        "advisory_date_range": advisory_date_range,
        "high_impact_pct": high_impact_pct,
    }


def render_template(template_name: str, data: dict) -> str:
    """Render a Jinja2 template with the given data."""
    env = Environment(
        loader=FileSystemLoader(str(TEMPLATES_DIR)),
        keep_trailing_newline=True,
        trim_blocks=True,
        lstrip_blocks=True,
    )
    template = env.get_template(template_name)
    return template.render(**data)


def main():
    local_only = "--local" in sys.argv

    print("=" * 60)
    print("OpenClaw CVE & GHSA Tracker — README Update")
    print("=" * 60)

    data = collect_data(local_only=local_only)

    print(f"\nStats: {data['counts']['total_ghsas']} GHSAs, "
          f"{data['counts']['total_cves']} CVEs assigned, "
          f"{data['counts']['cves_published']} published in cvelistV5")

    # Render README
    readme_content = render_template("README.md.j2", data)
    readme_path = ROOT / "README.md"
    with open(readme_path, "w") as f:
        f.write(readme_content)
    print(f"\n✅ README.md updated ({len(readme_content)} bytes)")

    # Render ADVISORIES.md
    advisories_content = render_template("ADVISORIES.md.j2", data)
    advisories_path = ROOT / "ADVISORIES.md"
    with open(advisories_path, "w") as f:
        f.write(advisories_content)
    print(f"✅ ADVISORIES.md updated ({len(advisories_content)} bytes)")

    print(f"   Last updated: {data['updated_at']}")


if __name__ == "__main__":
    main()
