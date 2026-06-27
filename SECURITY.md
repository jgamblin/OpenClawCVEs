# Security Policy

## Reporting a Vulnerability

This repository is a **read-only security tracker** — it aggregates and presents publicly available CVE and GHSA data for the [OpenClaw](https://github.com/openclaw/openclaw) project. It does not contain any OpenClaw application code.

### If you found a vulnerability in OpenClaw itself

Please report it directly to the OpenClaw project:

- **GitHub Security Advisories:** [openclaw/openclaw → Report a vulnerability](https://github.com/openclaw/openclaw/security/advisories/new)
- **Repository:** [github.com/openclaw/openclaw](https://github.com/openclaw/openclaw)

### If you found an issue with this tracker

If you've found a bug in this tracker's automation (e.g., incorrect data, missing advisories, script errors), please [open an issue](https://github.com/jgamblin/OpenClawCVEs/issues/new).

## Scope

This tracker monitors:

- [GitHub Advisory Database](https://github.com/advisories?query=openclaw) entries for `openclaw`, `clawdbot`, and `moltbot`
- [CVEProject/cvelistV5](https://github.com/CVEProject/cvelistV5) — a **full scan** of the registry for every CVE whose affected product is OpenClaw, **regardless of which CNA assigned it** (most are assigned by [VulnCheck](https://vulncheck.com), not the project itself)
- [Repo-level security advisories](https://github.com/openclaw/openclaw/security/advisories) on the OpenClaw repository

## Coordinated Disclosure

All vulnerabilities listed in this tracker are public records. Project-issued advisories were disclosed through GitHub's coordinated disclosure process; third-party CVEs are sourced from their published CVE List V5 records. We do not publish vulnerability details beyond what is already public in the referenced GHSAs and CVE records.
