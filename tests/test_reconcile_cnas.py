"""
Tests for reconcile_cnas.py — the full CVE List V5 / by-CNA scanner.

Pure-function coverage only (no network/clone): matching, per-record summary,
and aggregation. Run with: pytest tests/ -v
"""

import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT))

from reconcile_cnas import (
    match_openclaw,
    summarize_record,
    aggregate,
)


def _record(vendor=None, product=None, assigner="VulnCheck", state="PUBLISHED",
            cve_id="CVE-2026-00001", published="2026-03-18T00:00:00.000Z",
            affected_extra=None):
    """Build a minimal cvelistV5-shaped record."""
    aff = {}
    if vendor is not None:
        aff["vendor"] = vendor
    if product is not None:
        aff["product"] = product
    if affected_extra:
        aff.update(affected_extra)
    return {
        "cveMetadata": {
            "cveId": cve_id,
            "assignerShortName": assigner,
            "state": state,
            "datePublished": published,
        },
        "containers": {"cna": {"affected": [aff]}},
    }


# ─── match_openclaw ──────────────────────────────────────────────────────────


class TestMatchOpenclaw:
    def test_vendor_match(self):
        assert match_openclaw(_record(vendor="openclaw"))

    def test_product_match(self):
        assert match_openclaw(_record(product="OpenClaw"))

    def test_case_and_whitespace_insensitive(self):
        assert match_openclaw(_record(vendor="  OpenClaw  "))

    def test_former_names_match(self):
        assert match_openclaw(_record(product="clawdbot"))
        assert match_openclaw(_record(vendor="moltbot"))

    def test_repo_ref_match(self):
        rec = _record(vendor="someone", product="thing", affected_extra={
            "repo": "https://github.com/openclaw/openclaw"
        })
        assert match_openclaw(rec)

    def test_collection_url_match(self):
        rec = _record(vendor="x", affected_extra={
            "collectionURL": "https://github.com/OpenClaw/OpenClaw"
        })
        assert match_openclaw(rec)

    def test_no_match(self):
        assert not match_openclaw(_record(vendor="acme", product="widget"))

    def test_missing_affected(self):
        assert not match_openclaw({"containers": {"cna": {}}})
        assert not match_openclaw({})

    def test_non_dict_affected_entry_ignored(self):
        rec = {"containers": {"cna": {"affected": ["junk", None]}}}
        assert not match_openclaw(rec)


# ─── summarize_record ────────────────────────────────────────────────────────


class TestSummarizeRecord:
    def test_basic_fields(self):
        row = summarize_record(_record(vendor="openclaw", assigner="VulnCheck"))
        assert row["cve_id"] == "CVE-2026-00001"
        assert row["assigner"] == "VulnCheck"
        assert row["date_published"] == "2026-03-18"
        assert row["state"] == "PUBLISHED"
        assert row["source"] == "cvelistV5"

    def test_rejected_excluded(self):
        assert summarize_record(_record(state="REJECTED")) is None

    def test_rejected_case_insensitive(self):
        assert summarize_record(_record(state="rejected")) is None

    def test_missing_assigner_defaults(self):
        rec = _record(vendor="openclaw")
        rec["cveMetadata"]["assignerShortName"] = ""
        assert summarize_record(rec)["assigner"] == "unknown"


# ─── aggregate ───────────────────────────────────────────────────────────────


class TestAggregate:
    def _rows(self):
        return [
            summarize_record(_record(cve_id="CVE-2026-0001", assigner="VulnCheck",
                                     published="2026-03-01T00:00:00Z")),
            summarize_record(_record(cve_id="CVE-2026-0002", assigner="VulnCheck",
                                     published="2026-03-15T00:00:00Z")),
            summarize_record(_record(cve_id="CVE-2026-0003", assigner="GitHub_M",
                                     published="2026-04-02T00:00:00Z")),
            summarize_record(_record(cve_id="CVE-2026-0004", assigner="zdi",
                                     published="2026-04-10T00:00:00Z")),
        ]

    def test_total(self):
        result = aggregate(self._rows(), set())
        assert result["total"] == 4

    def test_by_assigner_sorted_desc_with_pct(self):
        result = aggregate(self._rows(), set())
        top = result["by_assigner"][0]
        assert top["cna"] == "VulnCheck"
        assert top["count"] == 2
        assert top["pct"] == 50.0
        # Sorted descending by count
        counts = [a["count"] for a in result["by_assigner"]]
        assert counts == sorted(counts, reverse=True)

    def test_project_vs_third_party_split(self):
        result = aggregate(self._rows(), set())
        assert result["project_issued"] == 1          # GitHub_M
        assert result["third_party_issued"] == 3       # VulnCheck x2 + zdi

    def test_monthly_bucketing(self):
        result = aggregate(self._rows(), set())
        months = {m["month"]: m["count"] for m in result["monthly_2026"]}
        assert months == {"2026-03": 2, "2026-04": 2}

    def test_ghsa_intersection_marks_rows(self):
        rows = self._rows()
        aggregate(rows, {"CVE-2026-0003"})
        flagged = {r["cve_id"]: r["in_ghsa_pipeline"] for r in rows}
        assert flagged["CVE-2026-0003"] is True
        assert flagged["CVE-2026-0001"] is False
        # Rows present in the GHSA pipeline get a combined source tag
        ghsa_row = next(r for r in rows if r["cve_id"] == "CVE-2026-0003")
        assert ghsa_row["source"] == "cvelistV5+ghsa"

    def test_empty(self):
        result = aggregate([], set())
        assert result["total"] == 0
        assert result["by_assigner"] == []
        assert result["monthly_2026"] == []
        assert result["project_issued"] == 0
        assert result["third_party_issued"] == 0
