#!/usr/bin/env bash
# fetch-openclaw-cves.sh — Search the CVEProject/cvelistV5 GitHub repo for
# CVEs related to OpenClaw (and its previous names) and output a JSON summary.
#
# Requirements: gh (GitHub CLI, authenticated), jq, base64
# Usage: ./fetch-openclaw-cves.sh [--json] [--raw]
#
# Flags:
#   --json  Output machine-readable JSON array
#   --raw   Dump full CVE records (one file per CVE in ./cve-records/)

set -euo pipefail

REPO="CVEProject/cvelistV5"
SEARCH_TERMS=("openclaw" "clawdbot" "moltbot" "clawhub")
OUTPUT_JSON=false
OUTPUT_RAW=false

for arg in "$@"; do
  case "$arg" in
    --json) OUTPUT_JSON=true ;;
    --raw)  OUTPUT_RAW=true ;;
  esac
done

# ---------- Step 1: Collect unique CVE file paths ----------
declare -A seen_paths
all_paths=()

for term in "${SEARCH_TERMS[@]}"; do
  while IFS= read -r path; do
    if [[ -n "$path" && -z "${seen_paths[$path]:-}" ]]; then
      seen_paths["$path"]=1
      all_paths+=("$path")
    fi
  done < <(
    gh api search/code -X GET \
      -f "q=${term} repo:${REPO}" \
      -f per_page=100 \
      --jq '.items[].path' 2>/dev/null || true
  )
done

if [[ ${#all_paths[@]} -eq 0 ]]; then
  echo "No CVEs found for search terms: ${SEARCH_TERMS[*]}" >&2
  exit 0
fi

echo "Found ${#all_paths[@]} unique CVE record(s)." >&2

# ---------- Step 2: Fetch and parse each CVE record ----------
if $OUTPUT_RAW; then
  mkdir -p cve-records
fi

json_results="[]"

for path in "${all_paths[@]}"; do
  cve_id=$(basename "$path" .json)
  echo "Fetching $cve_id ..." >&2

  raw=$(gh api "repos/${REPO}/contents/${path}" --jq '.content' | base64 -d)

  if $OUTPUT_RAW; then
    echo "$raw" | python3 -m json.tool > "cve-records/${cve_id}.json" 2>/dev/null || \
      echo "$raw" > "cve-records/${cve_id}.json"
  fi

  # Extract key fields with jq
  record=$(echo "$raw" | jq -c '{
    cveId:        .cveMetadata.cveId,
    state:        .cveMetadata.state,
    datePublished: .cveMetadata.datePublished,
    dateUpdated:   .cveMetadata.dateUpdated,
    assignerShortName: .cveMetadata.assignerShortName,
    title:        .containers.cna.title,
    description:  (.containers.cna.descriptions[0].value // ""),
    vendor:       (.containers.cna.affected[0].vendor // ""),
    product:      (.containers.cna.affected[0].product // ""),
    packageURL:   (.containers.cna.affected[0].packageURL // ""),
    affectedVersions: (.containers.cna.affected[0].versions // []),
    cvss:         (.containers.cna.metrics[0].cvssV3_1.baseScore // null),
    severity:     (.containers.cna.metrics[0].cvssV3_1.baseSeverity // ""),
    vectorString: (.containers.cna.metrics[0].cvssV3_1.vectorString // ""),
    cwes:         [.containers.cna.problemTypes[]?.descriptions[]? | {cweId, description}],
    references:   [.containers.cna.references[]?.url],
    advisory:     (.containers.cna.source.advisory // ""),
    cisaSsvc:     (.containers.adp[]? | select(.title == "CISA ADP Vulnrichment") | .metrics[0].other.content.options // null)
  }')

  json_results=$(echo "$json_results" | jq --argjson r "$record" '. += [$r]')
done

# ---------- Step 3: Output ----------
if $OUTPUT_JSON; then
  echo "$json_results" | jq '.'
else
  # Human-readable table
  echo ""
  echo "═══════════════════════════════════════════════════════════════════════"
  echo "  OpenClaw CVE Summary (searched: ${SEARCH_TERMS[*]})"
  echo "  Source: github.com/${REPO}"
  echo "  Date: $(date -u '+%Y-%m-%d %H:%M UTC')"
  echo "═══════════════════════════════════════════════════════════════════════"
  echo ""

  echo "$json_results" | jq -r '
    sort_by(.cvss) | reverse | .[] |
    "──────────────────────────────────────────────────────────────────────\n" +
    "  \(.cveId)  [\(.severity // "N/A") — CVSS \(.cvss // "N/A")]\n" +
    "  Title:     \(.title // .description[0:80])\n" +
    "  Vendor:    \(.vendor)/\(.product)" +
      (if .packageURL != "" then "  (PURL: \(.packageURL))" else "" end) + "\n" +
    "  Versions:  \(.affectedVersions | map(.version // (.version // "?")) | join(", "))\n" +
    "  CWEs:      \(.cwes | map(.cweId) | join(", "))\n" +
    "  Published: \(.datePublished)  Updated: \(.dateUpdated)\n" +
    "  Assigner:  \(.assignerShortName)  Advisory: \(.advisory)\n" +
    "  Refs:      \(.references | join("\n             "))"
  '

  echo ""
  echo "──────────────────────────────────────────────────────────────────────"
  total=$(echo "$json_results" | jq length)
  high=$(echo "$json_results" | jq '[.[] | select(.cvss >= 7.0)] | length')
  medium=$(echo "$json_results" | jq '[.[] | select(.cvss >= 4.0 and .cvss < 7.0)] | length')
  echo "  Total: $total  |  High: $high  |  Medium: $medium"
  echo "══════════════════════════════════════════════════════════════════════"
fi
