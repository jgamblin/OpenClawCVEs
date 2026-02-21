"""
Tests for update_readme.py — parsing, rendering, and data logic.

Run with: pytest tests/ -v
"""

import json
import sys
from pathlib import Path

import pytest

# Make the project root importable
ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT))

from update_readme import (
    parse_cve_record,
    parse_ghsa_summary,
    render_template,
    load_repo_only_ghsas,
    severity_badge,
)


# ─── Fixtures ────────────────────────────────────────────────────────────────

SAMPLE_CVE_RECORD = {
    "dataType": "CVE_RECORD",
    "dataVersion": "5.2",
    "cveMetadata": {
        "cveId": "CVE-2026-24763",
        "assignerOrgId": "a0819718-46f1-4df5-94e2-005712e83aaa",
        "state": "PUBLISHED",
        "assignerShortName": "GitHub_M",
        "dateReserved": "2026-01-26T21:06:47.867Z",
        "datePublished": "2026-02-02T21:53:07.640Z",
        "dateUpdated": "2026-02-04T16:53:56.345Z",
    },
    "containers": {
        "cna": {
            "title": "Authenticated Command Injection in OpenClaw Docker Execution via PATH Environment Variable",
            "problemTypes": [
                {
                    "descriptions": [
                        {
                            "cweId": "CWE-78",
                            "lang": "en",
                            "description": "CWE-78: Improper Neutralization of Special Elements used in an OS Command ('OS Command Injection')",
                            "type": "CWE",
                        }
                    ]
                }
            ],
            "metrics": [
                {
                    "cvssV3_1": {
                        "attackComplexity": "LOW",
                        "attackVector": "NETWORK",
                        "availabilityImpact": "HIGH",
                        "baseScore": 8.8,
                        "baseSeverity": "HIGH",
                        "confidentialityImpact": "HIGH",
                        "integrityImpact": "HIGH",
                        "privilegesRequired": "LOW",
                        "scope": "UNCHANGED",
                        "userInteraction": "NONE",
                        "vectorString": "CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H",
                        "version": "3.1",
                    }
                }
            ],
            "references": [
                {
                    "name": "https://github.com/openclaw/openclaw/security/advisories/GHSA-mc68-q9jw-2h3v",
                    "tags": ["x_refsource_CONFIRM"],
                    "url": "https://github.com/openclaw/openclaw/security/advisories/GHSA-mc68-q9jw-2h3v",
                },
                {
                    "name": "https://github.com/openclaw/openclaw/commit/771f23d3",
                    "tags": ["x_refsource_MISC"],
                    "url": "https://github.com/openclaw/openclaw/commit/771f23d36b95ec2204cc9a0054045f5d8439ea75",
                },
            ],
            "affected": [
                {
                    "vendor": "clawdbot",
                    "product": "clawdbot",
                    "versions": [{"version": "< 2026.1.29", "status": "affected"}],
                }
            ],
            "descriptions": [
                {
                    "lang": "en",
                    "value": "OpenClaw (formerly  Clawdbot) is a personal AI assistant you run on your own devices. Prior to 2026.1.29, a command injection vulnerability existed.",
                }
            ],
            "source": {"advisory": "GHSA-mc68-q9jw-2h3v", "discovery": "UNKNOWN"},
        },
        "adp": [
            {
                "metrics": [
                    {
                        "other": {
                            "type": "ssvc",
                            "content": {
                                "id": "CVE-2026-24763",
                                "options": {
                                    "Exploitation": "none",
                                    "Automatable": "no",
                                    "Technical Impact": "total",
                                },
                                "role": "CISA Coordinator",
                                "version": "2.0.3",
                            },
                        }
                    }
                ],
                "title": "CISA ADP Vulnrichment",
                "providerMetadata": {
                    "orgId": "134c704f-9b21-4f2e-91b3-4a467353bcc0",
                    "shortName": "CISA-ADP",
                    "dateUpdated": "2026-02-04T16:53:56.345Z",
                },
            }
        ],
    },
}

SAMPLE_GHSA_WITH_CVE = {
    "ghsa_id": "GHSA-xwjm-j929-xq7c",
    "cve_id": "CVE-2026-26972",
    "html_url": "https://github.com/advisories/GHSA-xwjm-j929-xq7c",
    "summary": "OpenClaw has a Path Traversal in Browser Download Functionality",
    "severity": "medium",
    "published_at": "2026-02-18T17:37:52Z",
    "vulnerabilities": [
        {
            "package": {"ecosystem": "npm", "name": "openclaw"},
            "vulnerable_version_range": ">= 2026.1.12, <= 2026.2.12",
            "first_patched_version": "2026.2.13",
        }
    ],
    "cwes": [{"cwe_id": "CWE-22", "name": "Improper Limitation of a Pathname"}],
}

SAMPLE_GHSA_NO_CVE = {
    "ghsa_id": "GHSA-h9g4-589h-68xv",
    "cve_id": None,
    "html_url": "https://github.com/advisories/GHSA-h9g4-589h-68xv",
    "summary": "OpenClaw has an authentication bypass in sandbox browser bridge server",
    "severity": "high",
    "published_at": "2026-02-18T17:45:31Z",
    "vulnerabilities": [
        {
            "package": {"ecosystem": "npm", "name": "openclaw"},
            "vulnerable_version_range": ">= 2026.1.29-beta.1, < 2026.2.14",
        }
    ],
    "cwes": [{"cwe_id": "CWE-306", "name": "Missing Authentication for Critical Function"}],
}


# ─── Tests: parse_cve_record ─────────────────────────────────────────────────


class TestParseCveRecord:
    def test_basic_fields(self):
        result = parse_cve_record(SAMPLE_CVE_RECORD)
        assert result["cve_id"] == "CVE-2026-24763"
        assert result["state"] == "PUBLISHED"
        assert result["date_published"] == "2026-02-02"
        assert result["assigner"] == "GitHub_M"

    def test_title(self):
        result = parse_cve_record(SAMPLE_CVE_RECORD)
        assert "Command Injection" in result["title"]
        assert "OpenClaw" in result["title"]

    def test_cvss(self):
        result = parse_cve_record(SAMPLE_CVE_RECORD)
        assert result["cvss"] == 8.8
        assert result["severity"] == "HIGH"
        assert "CVSS:3.1" in result["vector_string"]

    def test_cwes(self):
        result = parse_cve_record(SAMPLE_CVE_RECORD)
        assert "CWE-78" in result["cwes"]
        assert "CWE-78" in result["cwes_long"]
        assert "OS Command" in result["cwes_long"]

    def test_affected(self):
        result = parse_cve_record(SAMPLE_CVE_RECORD)
        assert result["vendor"] == "clawdbot"
        assert result["product"] == "clawdbot"
        assert result["affected_versions"] == "< 2026.1.29"

    def test_ghsa_id_from_advisory_url(self):
        result = parse_cve_record(SAMPLE_CVE_RECORD)
        assert result["ghsa_id"] == "GHSA-mc68-q9jw-2h3v"
        assert "advisories/GHSA-mc68" in result["advisory_url"]

    def test_cisa_ssvc(self):
        result = parse_cve_record(SAMPLE_CVE_RECORD)
        assert "Exploitation: none" in result["cisa_ssvc"]
        assert "Automatable: no" in result["cisa_ssvc"]
        assert "Technical Impact: total" in result["cisa_ssvc"]

    def test_naming_note_old_name(self):
        result = parse_cve_record(SAMPLE_CVE_RECORD)
        assert result["naming_note"]  # Should have a note about old name
        assert "clawdbot" in result["naming_note"].lower()

    def test_description(self):
        result = parse_cve_record(SAMPLE_CVE_RECORD)
        assert "command injection" in result["description"].lower()

    def test_no_double_less_than(self):
        """Affected versions starting with < should not get double < <."""
        result = parse_cve_record(SAMPLE_CVE_RECORD)
        assert "< <" not in result["affected_versions"]

    def test_empty_record(self):
        """Parsing an empty/minimal record should not crash."""
        result = parse_cve_record({"cveMetadata": {}, "containers": {"cna": {}}})
        assert result["cve_id"] == ""
        assert result["cvss"] is None
        assert result["title"] == ""

    def test_fallback_title_from_description(self):
        """When title is missing, first sentence of description is used."""
        record = {
            "cveMetadata": {"cveId": "CVE-2026-99999", "state": "PUBLISHED"},
            "containers": {
                "cna": {
                    "descriptions": [
                        {"lang": "en", "value": "A critical flaw exists. More details follow."}
                    ]
                }
            },
        }
        result = parse_cve_record(record)
        assert result["title"] == "A critical flaw exists"


# ─── Tests: parse_ghsa_summary ───────────────────────────────────────────────


class TestParseGhsaSummary:
    def test_with_cve(self):
        result = parse_ghsa_summary(SAMPLE_GHSA_WITH_CVE)
        assert result["ghsa_id"] == "GHSA-xwjm-j929-xq7c"
        assert result["cve_id"] == "CVE-2026-26972"
        assert result["severity"] == "medium"
        assert "Path Traversal" in result["title"]
        assert result["published"] == "2026-02-18"
        assert result["fixed_version"] == "2026.2.13"

    def test_without_cve(self):
        result = parse_ghsa_summary(SAMPLE_GHSA_NO_CVE)
        assert result["ghsa_id"] == "GHSA-h9g4-589h-68xv"
        assert result["cve_id"] is None
        assert result["severity"] == "high"
        assert result["fixed_version"] in ("", None)

    def test_packages(self):
        result = parse_ghsa_summary(SAMPLE_GHSA_WITH_CVE)
        assert "npm/openclaw" in result["packages"]

    def test_cwes(self):
        result = parse_ghsa_summary(SAMPLE_GHSA_WITH_CVE)
        assert "CWE-22" in result["cwes"]

    def test_affected_versions(self):
        result = parse_ghsa_summary(SAMPLE_GHSA_WITH_CVE)
        assert len(result["affected_versions"]) > 0
        assert ">= 2026.1.12" in result["affected_versions"][0]

    def test_empty_advisory(self):
        """Parsing a minimal advisory should not crash."""
        result = parse_ghsa_summary({})
        assert result["ghsa_id"] == ""
        assert result["cve_id"] is None
        assert result["title"] == ""


# ─── Tests: load_repo_only_ghsas ─────────────────────────────────────────────


class TestLoadRepoOnlyGhsas:
    def test_loads_file(self):
        ghsas = load_repo_only_ghsas()
        assert len(ghsas) > 0
        # Each entry should have required fields
        for g in ghsas:
            assert "ghsa_id" in g
            assert "severity" in g
            assert "title" in g
            assert "html_url" in g
            assert g["ghsa_id"].startswith("GHSA-")

    def test_severities_are_valid(self):
        ghsas = load_repo_only_ghsas()
        valid = {"CRITICAL", "HIGH", "MODERATE", "MEDIUM", "LOW"}
        for g in ghsas:
            assert g["severity"].upper() in valid, f"Invalid severity: {g['severity']}"


# ─── Tests: severity_badge ───────────────────────────────────────────────────


class TestSeverityBadge:
    def test_critical(self):
        result = severity_badge("CRITICAL")
        assert "CRITICAL" in result
        assert "img.shields.io" in result

    def test_high(self):
        result = severity_badge("HIGH")
        assert "HIGH" in result

    def test_medium(self):
        result = severity_badge("medium")
        assert "MEDIUM" in result.upper()

    def test_low(self):
        result = severity_badge("Low")
        assert "LOW" in result.upper()

    def test_unknown_passthrough(self):
        result = severity_badge("custom")
        assert result == "CUSTOM"


# ─── Tests: render_template ──────────────────────────────────────────────────


class TestRenderTemplate:
    @pytest.fixture
    def sample_data(self):
        """Minimal data dict that exercises the template."""
        return {
            "updated_at": "2026-02-18 12:00 UTC",
            "counts": {
                "total_ghsas": 84,
                "total_cves": 20,
                "cves_published": 5,
                "cves_reserved": 15,
                "ghsas_no_cve": 64,
                "ghsas_indexed_no_cve": 35,
                "severity_critical": 3,
                "severity_high": 25,
                "severity_medium": 20,
                "severity_low": 2,
                "repo_only": 29,
            },
            "published_cves": [
                {
                    "cve_id": "CVE-2026-24763",
                    "state": "PUBLISHED",
                    "date_published": "2026-02-02",
                    "assigner": "GitHub_M",
                    "title": "Command Injection in Docker Execution",
                    "description": "A vulnerability exists.",
                    "cvss": 8.8,
                    "severity": "HIGH",
                    "vector_string": "CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H",
                    "cwes": "CWE-78",
                    "cwes_long": "CWE-78 (OS Command Injection)",
                    "vendor": "clawdbot",
                    "product": "clawdbot",
                    "purl": None,
                    "affected_versions": "< 2026.1.29",
                    "advisory_url": "https://github.com/openclaw/openclaw/security/advisories/GHSA-mc68-q9jw-2h3v",
                    "ghsa_id": "GHSA-mc68-q9jw-2h3v",
                    "references": [],
                    "cisa_ssvc": "Exploitation: none · Automatable: no",
                    "naming_note": "Uses old name clawdbot.",
                    "desc_names": "OpenClaw",
                    "severity_badge": severity_badge("HIGH"),
                },
            ],
            "pipeline_status": [
                {
                    "cve_id": "CVE-2026-24763",
                    "state": "PUBLISHED",
                    "in_cvelist": True,
                    "ghsa_published": "2026-02-02",
                    "cna": "GitHub_M",
                },
            ],
            "ghsas_with_cve": [
                {
                    "ghsa_id": "GHSA-xwjm-j929-xq7c",
                    "cve_id": "CVE-2026-26972",
                    "severity": "medium",
                    "title": "Path Traversal in Browser Download",
                    "published": "2026-02-18",
                    "html_url": "https://github.com/advisories/GHSA-xwjm-j929-xq7c",
                    "severity_badge": severity_badge("medium"),
                },
            ],
            "ghsas_no_cve": [
                {
                    "ghsa_id": "GHSA-h9g4-589h-68xv",
                    "severity": "high",
                    "title": "Auth bypass in sandbox browser bridge",
                    "published": "2026-02-18",
                    "html_url": "https://github.com/advisories/GHSA-h9g4-589h-68xv",
                    "severity_badge": severity_badge("high"),
                },
            ],
            "ghsas_critical_high": [
                {
                    "ghsa_id": "GHSA-h9g4-589h-68xv",
                    "cve_id": None,
                    "severity": "high",
                    "title": "Auth bypass in sandbox browser bridge",
                    "published": "2026-02-18",
                    "html_url": "https://github.com/advisories/GHSA-h9g4-589h-68xv",
                    "severity_badge": severity_badge("high"),
                },
            ],
            "ghsas_medium": [
                {
                    "ghsa_id": "GHSA-xwjm-j929-xq7c",
                    "cve_id": "CVE-2026-26972",
                    "severity": "medium",
                    "title": "Path Traversal in Browser Download",
                    "published": "2026-02-18",
                    "html_url": "https://github.com/advisories/GHSA-xwjm-j929-xq7c",
                    "severity_badge": severity_badge("medium"),
                },
            ],
            "ghsas_low": [],
            "repo_only_ghsas": [
                {
                    "ghsa_id": "GHSA-gv46-4xfq-jv58",
                    "severity": "CRITICAL",
                    "title": "RCE via Node Invoke Approval Bypass",
                    "html_url": "https://github.com/openclaw/openclaw/security/advisories/GHSA-gv46-4xfq-jv58",
                    "severity_badge": severity_badge("CRITICAL"),
                },
            ],
            "naming_issues": [
                {
                    "cve_id": "CVE-2026-24763",
                    "vendor": "clawdbot",
                    "product": "clawdbot",
                    "purl": None,
                    "desc_names": "OpenClaw",
                },
            ],
            "vuln_categories": [
                {"name": "OS Command Injection (CWE-78)", "count": 5, "examples": "PATH injection"},
            ],
            "top_cwe": {
                "name": "OS Command Injection (CWE-78)",
                "count": 5,
                "total": 5,
                "pct": 100,
            },
            "sync_rate_pct": 25,
            "advisory_date_range": "2026-02-02 → 2026-02-18",
            "high_impact_pct": 33,
        }

    def _render(self, data):
        return render_template("README.md.j2", data)

    def test_renders_without_error(self, sample_data):
        output = self._render(sample_data)
        assert len(output) > 0

    def test_contains_dashboard_stats(self, sample_data):
        output = self._render(sample_data)
        assert "84" in output  # total_ghsas
        assert "20" in output  # total_cves

    def test_contains_cve_table(self, sample_data):
        output = self._render(sample_data)
        assert "CVE-2026-24763" in output
        assert "Command Injection" in output
        assert "8.8" in output

    def test_contains_shields_badges(self, sample_data):
        output = self._render(sample_data)
        assert "img.shields.io" in output

    def test_contains_mermaid_diagram(self, sample_data):
        output = self._render(sample_data)
        assert "```mermaid" in output

    def test_contains_pipeline(self, sample_data):
        output = self._render(sample_data)
        assert "PUBLISHED" in output

    def test_contains_ghsa_tables(self, sample_data):
        output = self._render(sample_data)
        assert "GHSA-xwjm-j929-xq7c" in output
        assert "GHSA-h9g4-589h-68xv" in output

    def test_contains_repo_only(self, sample_data):
        output = self._render(sample_data)
        assert "GHSA-gv46-4xfq-jv58" in output
        assert "Repo-Only" in output

    def test_contains_data_sources(self, sample_data):
        output = self._render(sample_data)
        assert "cvelistV5" in output
        assert "Advisory DB" in output

    def test_header_has_openclaw(self, sample_data):
        output = self._render(sample_data)
        assert "OpenClaw" in output

    def test_updated_at(self, sample_data):
        output = self._render(sample_data)
        assert "2026-02-18" in output

    def test_key_insights(self, sample_data):
        output = self._render(sample_data)
        assert "Key Insights" in output or "Insights" in output
        assert "OS Command Injection" in output  # top_cwe

    def test_severity_grouped(self, sample_data):
        output = self._render(sample_data)
        # Critical/High group should appear
        assert "Critical" in output or "CRITICAL" in output

    def test_advisories_md_renders(self, sample_data):
        output = render_template("ADVISORIES.md.j2", sample_data)
        assert len(output) > 0
        assert "GHSA-xwjm-j929-xq7c" in output
