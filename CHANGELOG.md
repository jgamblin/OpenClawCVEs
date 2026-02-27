# Changelog

All notable changes to the OpenClaw CVE & GHSA Tracker are documented here.

## [2026-02-27] — Accuracy overhaul: repo-advisory auto-sync & deduplication

### Bug Fixes

- **Fixed double-counting of GHSAs.**
  17 advisories appeared in both `ghsa-advisories.json` (global Advisory DB) and
  `repo-only-ghsas.json`, inflating the badge from the true count of 91 unique
  GHSAs to 108. The total is now computed from deduplicated sets.

- **Fixed 113+ missing GHSAs.**
  The script only queried the global GitHub Advisory Database API
  (`/advisories?affects=…`), which returns advisories that have been reviewed and
  published to the global DB. Many OpenClaw advisories exist only on the
  repository security page and were never picked up. The tracker now also queries
  the repo-level API to capture all advisories.

### New Features

- **Automatic repo-advisory sync.**
  `update_readme.py` now fetches all advisories from
  `/repos/openclaw/openclaw/security-advisories` (paginated) on every non-local
  run, deduplicates them against the global Advisory DB results, and saves the
  remainder to `repo-only-ghsas.json`. No manual maintenance of that file is
  needed anymore.

- **Repo-level CVE ID discovery.**
  CVE IDs assigned through repo advisories (but not yet visible in the global
  Advisory DB) are now captured and included in the tracker's CVE counts.

### Changed

- `update_readme.py` — Added `fetch_repo_advisories()` and
  `parse_repo_advisory_summary()` functions; rewrote the top of `collect_data()`
  to auto-refresh and deduplicate repo-only GHSAs; merged `repo_cve_ids` into
  the all-CVE-IDs set.
- `repo-only-ghsas.json` — Rebuilt: went from 29 entries (with 17 duplicates) to
  145 deduplicated entries.
- `README.md` / `ADVISORIES.md` — Regenerated with corrected counts.

### Verified Numbers

| Metric | Before | After |
|--------|--------|-------|
| Total GHSAs (badge) | 108 (inflated) | **224** |
| Advisory DB GHSAs | 79 | 79 |
| Repo-only GHSAs | 29 (17 dupes) | **145** (0 dupes) |
| Overlap | 17 | **0** |
| CVEs tracked | 34 | 34 |

## [2026-02-27b] — Repo-only GHSAs as first-class data

### Bug Fixes

- **CI workflow: `repo-only-ghsas.json` missing from change detection.**
  The "Check for changes" step in `update-readme.yml` did not include
  `repo-only-ghsas.json` in `git status --porcelain`, so if that file was the
  only one that changed the commit would be silently skipped. Fixed by adding it
  to the porcelain check.

- **CI workflow: `repo-only-ghsas.json` not cleaned before rebuild.**
  The "Clean generated files" step did not remove it, leaving a stale cache
  during the brief window before `collect_data()` overwrites it. Now cleaned
  alongside all other generated files.

### New Features

- **Published dates for repo-only GHSAs.**
  `parse_repo_advisory_summary()` now captures `published_at` as a `published`
  field (YYYY-MM-DD). Templates updated to show the Published column for
  repo-only advisories in both README.md and ADVISORIES.md.

- **New tests for `parse_repo_advisory_summary`.**
  7 unit tests covering basic fields, severity uppercasing, null/missing values,
  URL fallback, and newline stripping. Also added `test_published_dates_are_present`
  and `test_no_overlap_with_advisory_db` integration tests to `TestLoadRepoOnlyGhsas`.
  Total test count: 39 → 48.

### Removed

- **Deprecated shell scripts.**
  Removed `fetch-openclaw-cves.sh` and `fetch-openclaw-ghsas.sh`, which were
  already marked as deprecated and fully superseded by `update_readme.py`.
