# OpenClaw CVE Tracker

## Project Identity

| Field | Value |
|-------|-------|
| **Current Name** | OpenClaw |
| **Previous Names** | Moltbot (second name), Clawdbot (original name) |
| **Main Repo** | [openclaw/openclaw](https://github.com/openclaw/openclaw) |
| **npm Package** | `openclaw` (formerly `clawdbot`) |
| **Skill Registry** | [ClawHub](https://clawhub.com/) |
| **Description** | Personal AI assistant — runs on your devices, multichannel (WhatsApp, Telegram, Slack, Discord, Signal, iMessage, Teams, etc.) |
| **License** | MIT |
| **Primary Author** | Peter Steinberger ([steipete](https://github.com/steipete)) |

### Search Terms for CVE Discovery

To find all CVEs related to this project, search for **all** of these terms:

- `openclaw`
- `clawdbot`
- `moltbot`
- `clawhub`
- `pkg:npm/clawdbot`
- `pkg:npm/openclaw`

---

## CVE Inventory (as of 2026-02-18)

| CVE ID | Severity | CVSS | Title | Fixed In | CWE | Published | CNA |
|--------|----------|------|-------|----------|-----|-----------|-----|
| [CVE-2026-25593](https://github.com/openclaw/openclaw/security/advisories/GHSA-g55j-c2v4-pjcg) | **HIGH** | 8.4 | Unauthenticated Local RCE via WebSocket `config.apply` | 2026.1.20 | CWE-78, CWE-306 | 2026-02-06 | GitHub_M |
| [CVE-2026-24763](https://github.com/openclaw/openclaw/security/advisories/GHSA-mc68-q9jw-2h3v) | **HIGH** | 8.8 | Authenticated Command Injection in Docker Execution via PATH | 2026.1.29 | CWE-78 | 2026-02-02 | GitHub_M |
| [CVE-2026-25253](https://github.com/openclaw/openclaw/security/advisories/GHSA-g8p2-7wf7-98mq) | **HIGH** | 8.8 | 1-Click RCE — WebSocket auto-connect via `gatewayUrl` query string | 2026.1.29 | CWE-669 | 2026-02-01 | MITRE |
| [CVE-2026-25157](https://github.com/openclaw/openclaw/security/advisories/GHSA-q284-4pvr-m585) | **HIGH** | 7.8 | OS Command Injection via Project Root Path in `sshNodeCommand` | 2026.1.29 | CWE-78 | 2026-02-04 | GitHub_M |
| [CVE-2026-25475](https://github.com/openclaw/openclaw/security/advisories/GHSA-r8g4-86fx-92mq) | **MEDIUM** | 6.5 | Local File Inclusion via `MEDIA:` Path Extraction | 2026.1.30 | CWE-200, CWE-22 | 2026-02-04 | GitHub_M |

---

## Detailed CVE Analysis

### CVE-2026-25593 — Unauthenticated Local RCE via WebSocket `config.apply`

| Field | Detail |
|-------|--------|
| **CVSS** | 8.4 (HIGH) — `AV:L/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H` |
| **CWE** | CWE-78 (OS Command Injection), CWE-306 (Missing Authentication) |
| **Affected** | OpenClaw < 2026.1.20 |
| **Vendor/Product** | openclaw / openclaw |
| **Advisory** | [GHSA-g55j-c2v4-pjcg](https://github.com/openclaw/openclaw/security/advisories/GHSA-g55j-c2v4-pjcg) |
| **CISA SSVC** | Exploitation: none · Automatable: no · Technical Impact: total |

**Description:** An unauthenticated local client could use the Gateway WebSocket API to write config via `config.apply` and set unsafe `cliPath` values that were later used for command discovery, enabling command injection as the gateway user.

**Naming in CVE:** Listed under vendor/product `openclaw/openclaw`.

---

### CVE-2026-24763 — Authenticated Command Injection in Docker Execution via PATH

| Field | Detail |
|-------|--------|
| **CVSS** | 8.8 (HIGH) — `AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H` |
| **CWE** | CWE-78 (OS Command Injection) |
| **Affected** | OpenClaw < 2026.1.29 |
| **Vendor/Product** | clawdbot / clawdbot _(old name used!)_ |
| **Advisory** | [GHSA-mc68-q9jw-2h3v](https://github.com/openclaw/openclaw/security/advisories/GHSA-mc68-q9jw-2h3v) |
| **CISA SSVC** | Exploitation: none · Automatable: no · Technical Impact: total |

**Description:** A command injection vulnerability existed in OpenClaw's Docker sandbox execution mechanism due to unsafe handling of the PATH environment variable when constructing shell commands. An authenticated user able to control environment variables could influence command execution within the container context.

**Naming in CVE:** Listed under vendor/product `clawdbot/clawdbot` (the old project name). Description references "OpenClaw (formerly Clawdbot)".

---

### CVE-2026-25253 — 1-Click RCE via WebSocket Auto-Connect

| Field | Detail |
|-------|--------|
| **CVSS** | 8.8 (HIGH) — `AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H` |
| **CWE** | CWE-669 (Incorrect Resource Transfer Between Spheres) |
| **Affected** | OpenClaw < 2026.1.29 |
| **Vendor/Product** | OpenClaw / OpenClaw |
| **Package URL** | `pkg:npm/clawdbot` _(old npm package name!)_ |
| **Assigned by** | MITRE (not GitHub) |
| **Advisory** | [GHSA-g8p2-7wf7-98mq](https://github.com/openclaw/openclaw/security/advisories/GHSA-g8p2-7wf7-98mq) |
| **CISA SSVC** | Exploitation: **poc** · Automatable: no · Technical Impact: total |

**Description:** OpenClaw (aka clawdbot or Moltbot) before 2026.1.29 obtains a `gatewayUrl` value from a query string and automatically makes a WebSocket connection without prompting, sending a token value.

**Naming in CVE:** Uses **all three names** — "OpenClaw (aka clawdbot or Moltbot)". The `packageURL` field still references `pkg:npm/clawdbot`. This is the only CVE assigned by MITRE (the others are GitHub). This is also the **only CVE with a known proof-of-concept exploit** (CISA SSVC Exploitation: poc).

**External References:**
- [1-Click RCE blog post (depthfirst.com)](https://depthfirst.com/post/1-click-rce-to-steal-your-moltbot-data-and-keys)
- [Ethiack blog post](https://ethiack.com/news/blog/one-click-rce-moltbot)
- [X post by @0xacb](https://x.com/0xacb/status/2016913750557651228)

---

### CVE-2026-25157 — OS Command Injection via SSH Node Command

| Field | Detail |
|-------|--------|
| **CVSS** | 7.8 (HIGH) — `AV:L/AC:H/PR:N/UI:R/S:C/C:H/I:H/A:H` |
| **CWE** | CWE-78 (OS Command Injection) |
| **Affected** | OpenClaw < 2026.1.29 |
| **Vendor/Product** | openclaw / openclaw |
| **Advisory** | [GHSA-q284-4pvr-m585](https://github.com/openclaw/openclaw/security/advisories/GHSA-q284-4pvr-m585) |
| **CISA SSVC** | Exploitation: none · Automatable: no · Technical Impact: total |

**Description:** The `sshNodeCommand` function constructed a shell script without properly escaping the user-supplied project path in an error message. When `cd` failed, the unescaped path was interpolated directly into an `echo` statement, allowing arbitrary command execution on the remote SSH host. Additionally, `parseSSHTarget` did not validate that SSH target strings could not begin with a dash, so a target like `-oProxyCommand=...` would be interpreted as an SSH flag.

**Naming in CVE:** Title says "OpenClaw/Clawdbot", vendor/product is `openclaw/openclaw`.

---

### CVE-2026-25475 — Local File Inclusion via `MEDIA:` Path

| Field | Detail |
|-------|--------|
| **CVSS** | 6.5 (MEDIUM) — `AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:N/A:N` |
| **CWE** | CWE-200 (Information Exposure), CWE-22 (Path Traversal) |
| **Affected** | OpenClaw < 2026.1.30 |
| **Vendor/Product** | openclaw / openclaw |
| **Advisory** | [GHSA-r8g4-86fx-92mq](https://github.com/openclaw/openclaw/security/advisories/GHSA-r8g4-86fx-92mq) |
| **CISA SSVC** | Exploitation: none · Automatable: no · Technical Impact: partial |

**Description:** The `isValidMedia()` function in `src/media/parse.ts` allows arbitrary file paths including absolute paths, home directory paths, and directory traversal sequences. An agent can read any file on the system by outputting `MEDIA:/path/to/file`, exfiltrating sensitive data to the user/channel.

**Naming in CVE:** Consistent `openclaw/openclaw`.

---

## Naming Inconsistencies Across CVEs

A key finding is **inconsistent vendor/product naming** across the 5 CVEs:

| CVE | vendor | product | packageURL | Description Names |
|-----|--------|---------|------------|-------------------|
| CVE-2026-25593 | `openclaw` | `openclaw` | — | OpenClaw |
| CVE-2026-24763 | `clawdbot` | `clawdbot` | — | OpenClaw (formerly Clawdbot) |
| CVE-2026-25253 | `OpenClaw` | `OpenClaw` | `pkg:npm/clawdbot` | OpenClaw (aka clawdbot or Moltbot) |
| CVE-2026-25157 | `openclaw` | `openclaw` | — | OpenClaw |
| CVE-2026-25475 | `openclaw` | `openclaw` | — | OpenClaw |

**Issues:**
1. **CVE-2026-24763** uses the old name `clawdbot/clawdbot` as vendor/product despite the project being renamed.
2. **CVE-2026-25253** uses a `packageURL` of `pkg:npm/clawdbot` (old npm name) but vendor/product as `OpenClaw/OpenClaw` (with inconsistent casing vs. the others which use lowercase).
3. There is no standardized PURL across all records.
4. Four CVEs are assigned by **GitHub_M** (GitHub Security Advisory), one by **MITRE** directly.

---

## Summary Statistics

| Metric | Value |
|--------|-------|
| **Total CVEs** | 5 |
| **Critical (9.0+)** | 0 |
| **High (7.0-8.9)** | 4 |
| **Medium (4.0-6.9)** | 1 |
| **Low (0.1-3.9)** | 0 |
| **With PoC Exploit** | 1 (CVE-2026-25253) |
| **OS Command Injection (CWE-78)** | 3 |
| **Path Traversal (CWE-22)** | 1 |
| **Missing Auth (CWE-306)** | 1 |
| **Incorrect Resource Transfer (CWE-669)** | 1 |
| **Info Exposure (CWE-200)** | 1 |
| **First Published** | 2026-02-01 |
| **Latest Published** | 2026-02-06 |
| **All Fixed By** | 2026.1.30 |

---

## Data Source

All CVE data sourced from: [CVEProject/cvelistV5](https://github.com/CVEProject/cvelistV5)

File paths in the repository:
- `cves/2026/24xxx/CVE-2026-24763.json`
- `cves/2026/25xxx/CVE-2026-25157.json`
- `cves/2026/25xxx/CVE-2026-25253.json`
- `cves/2026/25xxx/CVE-2026-25475.json`
- `cves/2026/25xxx/CVE-2026-25593.json`
