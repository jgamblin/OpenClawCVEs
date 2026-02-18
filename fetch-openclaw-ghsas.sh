#!/usr/bin/env bash
# fetch-openclaw-ghsas.sh — Fetch all GitHub Security Advisories for OpenClaw
# (and its previous names) from the GitHub Advisory Database API.
#
# ⚠️  DEPRECATED: This script is superseded by update_readme.py, which fetches
# all CVE/GHSA data and renders the README automatically. Kept for reference
# and ad-hoc manual queries.
#
# Requirements: gh (GitHub CLI, authenticated), jq
# Usage: ./fetch-openclaw-ghsas.sh [--json]
#
# Flags:
#   --json  Output machine-readable JSON array (default: human-readable table)

set -euo pipefail

PACKAGES=("openclaw" "clawdbot" "moltbot")
OUTPUT_JSON=false

for arg in "$@"; do
  case "$arg" in
    --json) OUTPUT_JSON=true ;;
  esac
done

# ---------- Step 1: Collect all advisories across package names ----------
all_ghsas='[]'
for pkg in "${PACKAGES[@]}"; do
  page=1
  while true; do
    result=$(gh api "/advisories?affects=${pkg}&per_page=100&page=${page}" 2>/dev/null || echo "[]")
    count=$(echo "$result" | jq 'length')
    if [[ "$count" -eq 0 ]]; then break; fi
    all_ghsas=$(echo "$all_ghsas" "$result" | jq -s '.[0] + .[1]')
    if [[ "$count" -lt 100 ]]; then break; fi
    page=$((page + 1))
  done
done

# Deduplicate by ghsa_id
unique=$(echo "$all_ghsas" | jq '[group_by(.ghsa_id) | .[] | .[0]]')
total=$(echo "$unique" | jq 'length')
echo "Found $total unique advisories from GitHub Advisory Database." >&2

# ---------- Step 2: Extract summary ----------
summary=$(echo "$unique" | jq '[.[] | {
  ghsa_id,
  cve_id: .cve_id,
  severity,
  summary: (.summary | gsub("\n"; " ")),
  published_at: .published_at,
  updated_at: .updated_at,
  type,
  html_url,
  packages: [.vulnerabilities[].package | "\(.ecosystem)/\(.name)"],
  affected_versions: [.vulnerabilities[].vulnerable_version_range],
  cwes: [.cwes[]?.cwe_id]
}] | sort_by(.published_at) | reverse')

# ---------- Step 3: Output ----------
if $OUTPUT_JSON; then
  echo "$summary" | jq '.'
else
  echo ""
  echo "═══════════════════════════════════════════════════════════════════════"
  echo "  OpenClaw GHSA Advisory Summary"
  echo "  Packages searched: ${PACKAGES[*]}"
  echo "  Date: $(date -u '+%Y-%m-%d %H:%M UTC')"
  echo "═══════════════════════════════════════════════════════════════════════"
  echo ""

  # Severity summary
  echo "  Severity Breakdown:"
  echo "$summary" | jq -r 'group_by(.severity) | .[] | "    \(.[0].severity | ascii_upcase): \(length)"'
  echo ""

  has_cve=$(echo "$summary" | jq '[.[] | select(.cve_id != null)] | length')
  no_cve=$(echo "$summary" | jq '[.[] | select(.cve_id == null)] | length')
  echo "  With CVE:    $has_cve"
  echo "  Without CVE: $no_cve"
  echo ""

  # Table
  echo "$summary" | jq -r '.[] |
    "──────────────────────────────────────────────────────────────────────\n" +
    "  \(.ghsa_id)  [\(.severity | ascii_upcase)]" +
    (if .cve_id != null then "  → \(.cve_id)" else "  (no CVE)" end) + "\n" +
    "  \(.summary[0:100])\n" +
    "  Published: \(.published_at[0:10])  Packages: \(.packages | join(", "))"
  '

  echo ""
  echo "──────────────────────────────────────────────────────────────────────"
  echo "  Total: $total  |  With CVE: $has_cve  |  Awaiting CVE: $no_cve"
  echo "══════════════════════════════════════════════════════════════════════"
fi
