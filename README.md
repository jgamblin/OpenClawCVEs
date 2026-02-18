# 🛡️ OpenClaw CVE & Security Advisory Tracker

> **Automated security tracking for [OpenClaw](https://github.com/openclaw/openclaw)** (formerly Clawdbot / Moltbot) — the open-source personal AI assistant.

---

<table>
<tr>
<td align="center" width="25%">

### 🔴 92
**Total Security<br>Advisories**

</td>
<td align="center" width="25%">

### 🟠 21
**CVE IDs<br>Assigned**

</td>
<td align="center" width="25%">

### 🟢 5
**CVEs Published<br>in cvelistV5**

</td>
<td align="center" width="25%">

### ⏳ 16
**CVEs Reserved<br>(Pending)**

</td>
</tr>
</table>

<table>
<tr>
<td align="center" width="20%">

**5** Critical

</td>
<td align="center" width="20%">

**50** High

</td>
<td align="center" width="20%">

**32** Medium

</td>
<td align="center" width="20%">

**5** Low

</td>
<td align="center" width="20%">

**71** Awaiting CVE

</td>
</tr>
</table>

<sub>Last updated: 2026-02-18 17:48 UTC · Updates every hour via [GitHub Actions](.github/workflows/update-readme.yml)</sub>

---

## Project Identity

| Field | Value |
|-------|-------|
| **Current Name** | OpenClaw |
| **Previous Names** | Moltbot (second name), Clawdbot (original name) |
| **Repository** | [openclaw/openclaw](https://github.com/openclaw/openclaw) |
| **npm Package** | `openclaw` (formerly `clawdbot`) |
| **License** | MIT |

<details>
<summary><strong>Search terms for CVE discovery</strong></summary>

To find all CVEs, search for: `openclaw`, `clawdbot`, `moltbot`, `clawhub`, `pkg:npm/clawdbot`, `pkg:npm/openclaw`

</details>

---

## CVEs Published in cvelistV5 (5)

These CVEs have full records in the [CVEProject/cvelistV5](https://github.com/CVEProject/cvelistV5) repository:

| CVE ID | Severity | CVSS | Title | CWE | Published |
|--------|----------|------|-------|-----|-----------|
| [CVE-2026-24763](https://github.com/openclaw/openclaw/security/advisories/GHSA-mc68-q9jw-2h3v) | **HIGH** | 8.8 | OpenClaw/Clawdbot Docker Execution has Authenticated Command Injection via PATH Environment Variable | CWE-78 | 2026-02-02 |
| [CVE-2026-25253](https://github.com/openclaw/openclaw/security/advisories/GHSA-g8p2-7wf7-98mq) | **HIGH** | 8.8 | OpenClaw/Clawdbot has 1-Click RCE via Authentication Token Exfiltration From gatewayUrl | CWE-669 | 2026-02-01 |
| [CVE-2026-25593](https://github.com/openclaw/openclaw/security/advisories/GHSA-g55j-c2v4-pjcg) | **HIGH** | 8.4 | OpenClaw Affected by Unauthenticated Local RCE via WebSocket config.apply | CWE-78, CWE-306 | 2026-02-06 |
| [CVE-2026-25157](https://github.com/openclaw/openclaw/security/advisories/GHSA-q284-4pvr-m585) | **HIGH** | 7.8 | OpenClaw/Clawdbot has OS Command Injection via Project Root Path in sshNodeCommand | CWE-78 | 2026-02-04 |
| [CVE-2026-25475](https://github.com/openclaw/openclaw/security/advisories/GHSA-r8g4-86fx-92mq) | **MEDIUM** | 6.5 | OpenClaw Vulnerable to Local File Inclusion via MEDIA: Path Extraction | CWE-200, CWE-22 | 2026-02-04 |
<details>
<summary><strong>Detailed CVE Analysis (click to expand)</strong></summary>

### CVE-2026-24763 — OpenClaw/Clawdbot Docker Execution has Authenticated Command Injection via PATH Environment Variable

| Field | Detail |
|-------|--------|
| **CVSS** | 8.8 (HIGH) — `CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H` |
| **CWE** | CWE-78 (CWE-78: Improper Neutralization of Special Elements used in an OS Command ('OS Command Injection')) |
| **Affected** | < 2026.1.29 |
| **Vendor/Product** | clawdbot / clawdbot |
| **Advisory** | [GHSA-mc68-q9jw-2h3v](https://github.com/openclaw/openclaw/security/advisories/GHSA-mc68-q9jw-2h3v) |

OpenClaw (formerly  Clawdbot) is a personal AI assistant you run on your own devices. Prior to 2026.1.29, a command injection vulnerability existed in OpenClaw’s Docker sandbox execution mechanism due to unsafe handling of the PATH environment variable when constructing shell commands. An authenticated user able to control environment variables could influence command execution within the container context. This vulnerability is fixed in 2026.1.29.

> **Naming note:** Uses old name `clawdbot/clawdbot` as vendor/product.
**References:**
- [https://github.com/openclaw/openclaw/commit/771f23d36b95ec2204cc9a0054045f5d8439ea75](https://github.com/openclaw/openclaw/commit/771f23d36b95ec2204cc9a0054045f5d8439ea75)
- [https://github.com/openclaw/openclaw/releases/tag/v2026.1.29](https://github.com/openclaw/openclaw/releases/tag/v2026.1.29)
---

### CVE-2026-25253 — OpenClaw/Clawdbot has 1-Click RCE via Authentication Token Exfiltration From gatewayUrl

| Field | Detail |
|-------|--------|
| **CVSS** | 8.8 (HIGH) — `CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H` |
| **CWE** | CWE-669 (CWE-669 Incorrect Resource Transfer Between Spheres) |
| **Affected** | < 2026.1.29 |
| **Vendor/Product** | OpenClaw / OpenClaw |
| **Advisory** | [GHSA-g8p2-7wf7-98mq](https://github.com/openclaw/openclaw/security/advisories/GHSA-g8p2-7wf7-98mq) |

OpenClaw (aka clawdbot or Moltbot) before 2026.1.29 obtains a gatewayUrl value from a query string and automatically makes a WebSocket connection without prompting, sending a token value.

> **Naming note:** Uses all three names in description. packageURL still references `pkg:npm/clawdbot`.
**References:**
- [1-click-rce-to-steal-your-moltbot-data-and-keys](https://depthfirst.com/post/1-click-rce-to-steal-your-moltbot-data-and-keys)
- [blog](https://openclaw.ai/blog)
- [one-click-rce-moltbot](https://ethiack.com/news/blog/one-click-rce-moltbot)
- [2016913750557651228](https://x.com/0xacb/status/2016913750557651228)
---

### CVE-2026-25593 — OpenClaw Affected by Unauthenticated Local RCE via WebSocket config.apply

| Field | Detail |
|-------|--------|
| **CVSS** | 8.4 (HIGH) — `CVSS:3.1/AV:L/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H` |
| **CWE** | CWE-78 (CWE-78: Improper Neutralization of Special Elements used in an OS Command ('OS Command Injection')), CWE-306 (CWE-306: Missing Authentication for Critical Function) |
| **Affected** | < 2026.1.20 |
| **Vendor/Product** | openclaw / openclaw |
| **Advisory** | [GHSA-g55j-c2v4-pjcg](https://github.com/openclaw/openclaw/security/advisories/GHSA-g55j-c2v4-pjcg) |

OpenClaw is a personal AI assistant. Prior to 2026.1.20, an unauthenticated local client could use the Gateway WebSocket API to write config via config.apply and set unsafe cliPath values that were later used for command discovery, enabling command injection as the gateway user. This vulnerability is fixed in 2026.1.20.

---

### CVE-2026-25157 — OpenClaw/Clawdbot has OS Command Injection via Project Root Path in sshNodeCommand

| Field | Detail |
|-------|--------|
| **CVSS** | 7.8 (HIGH) — `CVSS:3.1/AV:L/AC:H/PR:N/UI:R/S:C/C:H/I:H/A:H` |
| **CWE** | CWE-78 (CWE-78: Improper Neutralization of Special Elements used in an OS Command ('OS Command Injection')) |
| **Affected** | < 2026.1.29 |
| **Vendor/Product** | openclaw / openclaw |
| **Advisory** | [GHSA-q284-4pvr-m585](https://github.com/openclaw/openclaw/security/advisories/GHSA-q284-4pvr-m585) |

OpenClaw is a personal AI assistant. Prior to version 2026.1.29, there is an OS command injection vulnerability via the Project Root Path in sshNodeCommand. The sshNodeCommand function constructed a shell script without properly escaping the user-supplied project path in an error message. When the cd command failed, the unescaped path was interpolated directly into an echo statement, allowing arbitrary command execution on the remote SSH host. The parseSSHTarget function did not validate that SSH target strings could not begin with a dash. An attacker-supplied target like -oProxyCommand=... would be interpreted as an SSH configuration flag rather than a hostname, allowing arbitrary command execution on the local machine. This issue has been patched in version 2026.1.29.

---

### CVE-2026-25475 — OpenClaw Vulnerable to Local File Inclusion via MEDIA: Path Extraction

| Field | Detail |
|-------|--------|
| **CVSS** | 6.5 (MEDIUM) — `CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:N/A:N` |
| **CWE** | CWE-200 (CWE-200: Exposure of Sensitive Information to an Unauthorized Actor), CWE-22 (CWE-22: Improper Limitation of a Pathname to a Restricted Directory ('Path Traversal')) |
| **Affected** | < 2026.1.30 |
| **Vendor/Product** | openclaw / openclaw |
| **Advisory** | [GHSA-r8g4-86fx-92mq](https://github.com/openclaw/openclaw/security/advisories/GHSA-r8g4-86fx-92mq) |

OpenClaw is a personal AI assistant. Prior to version 2026.1.30, the isValidMedia() function in src/media/parse.ts allows arbitrary file paths including absolute paths, home directory paths, and directory traversal sequences. An agent can read any file on the system by outputting MEDIA:/path/to/file, exfiltrating sensitive data to the user/channel. This issue has been patched in version 2026.1.30.

---

</details>

---

## CVE Publication Pipeline

Of 21 GHSAs with CVE IDs, **5** are fully published and **16** remain `RESERVED`.

```
┌─────────────┐     ┌─────────────────┐     ┌──────────────────┐     ┌─────────────┐
│  1. GitHub   │     │  2. GHSA goes   │     │  3. CNA submits  │     │ 4. cvelistV5│
│  reserves    │ ──► │  public with    │ ──► │  CVE record via  │ ──► │ bot commits │
│  CVE ID      │     │  CVE ID shown   │     │  CVE Services    │     │ JSON file   │
│ (RESERVED)   │     │                 │     │  (PUBLISHED)     │     │             │
└─────────────┘     └─────────────────┘     └──────────────────┘     └─────────────┘
```

| CVE ID | State | cvelistV5 | GHSA Published | CNA |
|--------|-------|-----------|----------------|-----|
| CVE-2026-24763 | **PUBLISHED** | ✅ | 2026-02-02 | GitHub_M |
| CVE-2026-24764 | RESERVED | ❌ | 2026-02-17 | — |
| CVE-2026-25157 | **PUBLISHED** | ✅ | 2026-02-02 | GitHub_M |
| CVE-2026-25253 | **PUBLISHED** | ✅ | 2026-02-02 | mitre |
| CVE-2026-25474 | RESERVED | ❌ | 2026-02-17 | — |
| CVE-2026-25475 | **PUBLISHED** | ✅ | 2026-02-04 | GitHub_M |
| CVE-2026-25593 | **PUBLISHED** | ✅ | 2026-02-04 | GitHub_M |
| CVE-2026-26316 | RESERVED | ❌ | 2026-02-17 | — |
| CVE-2026-26317 | RESERVED | ❌ | 2026-02-18 | — |
| CVE-2026-26319 | RESERVED | ❌ | 2026-02-17 | — |
| CVE-2026-26320 | RESERVED | ❌ | 2026-02-17 | — |
| CVE-2026-26321 | RESERVED | ❌ | 2026-02-17 | — |
| CVE-2026-26322 | RESERVED | ❌ | 2026-02-17 | — |
| CVE-2026-26323 | RESERVED | ❌ | 2026-02-18 | — |
| CVE-2026-26324 | RESERVED | ❌ | 2026-02-17 | — |
| CVE-2026-26325 | RESERVED | ❌ | 2026-02-17 | — |
| CVE-2026-26326 | RESERVED | ❌ | 2026-02-17 | — |
| CVE-2026-26327 | RESERVED | ❌ | 2026-02-18 | — |
| CVE-2026-26328 | RESERVED | ❌ | 2026-02-18 | — |
| CVE-2026-26329 | RESERVED | ❌ | 2026-02-18 | — |
| CVE-2026-26972 | RESERVED | ❌ | 2026-02-18 | — |
---

## All Security Advisories (92)

### GHSAs with CVE IDs (21)

| GHSA | CVE | Severity | Title | Published |
|------|-----|----------|-------|-----------|
| [GHSA-xwjm-j929-xq7c](https://github.com/advisories/GHSA-xwjm-j929-xq7c) | CVE-2026-26972 | MEDIUM | OpenClaw has a Path Traversal in Browser Download Functionality | 2026-02-18 |
| [GHSA-3fqr-4cg8-h96q](https://github.com/advisories/GHSA-3fqr-4cg8-h96q) | CVE-2026-26317 | HIGH | OpenClaw affected by cross-site request forgery (CSRF) through loopback browser mutation endpoints | 2026-02-18 |
| [GHSA-m7x8-2w3w-pr42](https://github.com/advisories/GHSA-m7x8-2w3w-pr42) | CVE-2026-26323 | HIGH | OpenClaw has a command injection in maintainer clawtributors updater | 2026-02-18 |
| [GHSA-cv7m-c9jx-vg7q](https://github.com/advisories/GHSA-cv7m-c9jx-vg7q) | CVE-2026-26329 | HIGH | OpenClaw has a path traversal in browser upload allows local file read | 2026-02-18 |
| [GHSA-g34w-4xqq-h79m](https://github.com/advisories/GHSA-g34w-4xqq-h79m) | CVE-2026-26328 | MEDIUM | OpenClaw iMessage group allowlist authorization inherited DM pairing-store identities | 2026-02-18 |
| [GHSA-pv58-549p-qh99](https://github.com/advisories/GHSA-pv58-549p-qh99) | CVE-2026-26327 | HIGH | OpenClaw allows unauthenticated discovery TXT records could steer routing and TLS pinning | 2026-02-18 |
| [GHSA-8mh7-phf8-xgfm](https://github.com/advisories/GHSA-8mh7-phf8-xgfm) | CVE-2026-26326 | MEDIUM | OpenClaw skills.status could leak secrets to operator.read clients | 2026-02-17 |
| [GHSA-h3f9-mjwj-w476](https://github.com/advisories/GHSA-h3f9-mjwj-w476) | CVE-2026-26325 | HIGH | OpenClaw Node host system.run rawCommand/command mismatch can bypass allowlist/approvals | 2026-02-17 |
| [GHSA-jrvc-8ff5-2f9f](https://github.com/advisories/GHSA-jrvc-8ff5-2f9f) | CVE-2026-26324 | HIGH | OpenClaw has a SSRF guard bypass via full-form IPv4-mapped IPv6 (loopback / metadata reachable) | 2026-02-17 |
| [GHSA-g6q9-8fvw-f7rf](https://github.com/advisories/GHSA-g6q9-8fvw-f7rf) | CVE-2026-26322 | HIGH | OpenClaw Gateway tool allowed unrestricted gatewayUrl override | 2026-02-17 |
| [GHSA-8jpq-5h99-ff5r](https://github.com/advisories/GHSA-8jpq-5h99-ff5r) | CVE-2026-26321 | HIGH | OpenClaw has a local file disclosure via sendMediaFeishu in Feishu extension | 2026-02-17 |
| [GHSA-7q2j-c4q5-rm27](https://github.com/advisories/GHSA-7q2j-c4q5-rm27) | CVE-2026-26320 | HIGH | OpenClaw macOS deep link confirmation truncation can conceal executed agent message | 2026-02-17 |
| [GHSA-4hg8-92x6-h2f3](https://github.com/advisories/GHSA-4hg8-92x6-h2f3) | CVE-2026-26319 | HIGH | OpenClaw is Missing Webhook Authentication in Telnyx Provider Allows Unauthenticated Requests | 2026-02-17 |
| [GHSA-pchc-86f6-8758](https://github.com/advisories/GHSA-pchc-86f6-8758) | CVE-2026-26316 | HIGH | OpenClaw BlueBubbles webhook auth bypass via loopback proxy trust | 2026-02-17 |
| [GHSA-mp5h-m6qj-6292](https://github.com/advisories/GHSA-mp5h-m6qj-6292) | CVE-2026-25474 | HIGH | OpenClaw has a Telegram webhook request forgery (missing `channels.telegram.webhookSecret`) → auth bypass | 2026-02-17 |
| [GHSA-782p-5fr5-7fj8](https://github.com/advisories/GHSA-782p-5fr5-7fj8) | CVE-2026-24764 | LOW | OpenClaw Affected by Remote Code Execution via System Prompt Injection in Slack Channel Descriptions | 2026-02-17 |
| [GHSA-g55j-c2v4-pjcg](https://github.com/advisories/GHSA-g55j-c2v4-pjcg) | CVE-2026-25593 | HIGH | OpenClaw vulnerable to Unauthenticated Local RCE via WebSocket config.apply | 2026-02-04 |
| [GHSA-r8g4-86fx-92mq](https://github.com/advisories/GHSA-r8g4-86fx-92mq) | CVE-2026-25475 | MEDIUM | OpenClaw Vulnerable to Local File Inclusion via MEDIA: Path Extraction | 2026-02-04 |
| [GHSA-q284-4pvr-m585](https://github.com/advisories/GHSA-q284-4pvr-m585) | CVE-2026-25157 | HIGH | OpenClaw/Clawdbot has OS Command Injection via Project Root Path in sshNodeCommand | 2026-02-02 |
| [GHSA-g8p2-7wf7-98mq](https://github.com/advisories/GHSA-g8p2-7wf7-98mq) | CVE-2026-25253 | HIGH | OpenClaw/Clawdbot has 1-Click RCE via Authentication Token Exfiltration From gatewayUrl | 2026-02-02 |
| [GHSA-mc68-q9jw-2h3v](https://github.com/advisories/GHSA-mc68-q9jw-2h3v) | CVE-2026-24763 | HIGH | OpenClaw/Clawdbot Docker Execution has Authenticated Command Injection via PATH Environment Variable | 2026-02-02 |
### GHSAs Without CVE — Potential Future CVEs (42)

| GHSA | Severity | Title | Published |
|------|----------|-------|-----------|
| [GHSA-qrq5-wjgg-rvqw](https://github.com/advisories/GHSA-qrq5-wjgg-rvqw) | **CRITICAL** | OpenClaw has a Path Traversal in Plugin Installation | 2026-02-17 |
| [GHSA-4rj2-gpmh-qq5x](https://github.com/advisories/GHSA-4rj2-gpmh-qq5x) | **CRITICAL** | OpenClaw has an inbound allowlist policy bypass in voice-call extension (empty caller ID + suffix matching) | 2026-02-17 |
| [GHSA-fhvm-j76f-qmjv](https://github.com/advisories/GHSA-fhvm-j76f-qmjv) | **CRITICAL** | OpenClaw has a potential access-group authorization bypass if channel type lookup fails | 2026-02-17 |
| [GHSA-rv39-79c4-7459](https://github.com/advisories/GHSA-rv39-79c4-7459) | **CRITICAL** | OpenClaw's gateway connect could skip device identity checks when auth.token was present but not yet validated | 2026-02-17 |
| [GHSA-r2c6-8jc8-g32w](https://github.com/advisories/GHSA-r2c6-8jc8-g32w) | HIGH | Duplicate Advisory: 1-Click RCE via Authentication Token Exfiltration From gatewayUrl | 2026-02-02 |
| [GHSA-mqpw-46fh-299h](https://github.com/advisories/GHSA-mqpw-46fh-299h) | HIGH | OpenClaw authorization bypass: operator.write can resolve exec approvals via chat.send -> /approve | 2026-02-17 |
| [GHSA-7vwx-582j-j332](https://github.com/advisories/GHSA-7vwx-582j-j332) | HIGH | OpenClaw MS Teams inbound attachment downloader leaks bearer tokens to allowlisted suffix domains | 2026-02-17 |
| [GHSA-33rq-m5x2-fvgf](https://github.com/advisories/GHSA-33rq-m5x2-fvgf) | HIGH | OpenClaw Twitch allowFrom is not enforced in optional plugin, unauthorized chat users can trigger agent pipeline | 2026-02-17 |
| [GHSA-56f2-hvwg-5743](https://github.com/advisories/GHSA-56f2-hvwg-5743) | HIGH | OpenClaw affected by SSRF in Image Tool Remote Fetch | 2026-02-17 |
| [GHSA-3hcm-ggvf-rch5](https://github.com/advisories/GHSA-3hcm-ggvf-rch5) | HIGH | OpenClaw has an exec allowlist bypass via command substitution/backticks inside double quotes | 2026-02-17 |
| [GHSA-mr32-vwc2-5j6h](https://github.com/advisories/GHSA-mr32-vwc2-5j6h) | HIGH | OpenClaw's Browser Relay /cdp websocket is missing auth which could allow cross-tab cookie access | 2026-02-17 |
| [GHSA-qj77-c3c8-9c3q](https://github.com/advisories/GHSA-qj77-c3c8-9c3q) | HIGH | OpenClaw's Windows cmd.exe parsing may bypass exec allowlist/approval gating | 2026-02-17 |
| [GHSA-64qx-vpxx-mvqf](https://github.com/advisories/GHSA-64qx-vpxx-mvqf) | HIGH | OpenClaw has an arbitrary transcript path file write via gateway sessionFile | 2026-02-17 |
| [GHSA-hv93-r4j3-q65f](https://github.com/advisories/GHSA-hv93-r4j3-q65f) | HIGH | OpenClaw Hook Session Key Override Enables Targeted Cross-Session Routing | 2026-02-17 |
| [GHSA-h9g4-589h-68xv](https://github.com/advisories/GHSA-h9g4-589h-68xv) | HIGH | OpenClaw has an authentication bypass in sandbox browser bridge server | 2026-02-18 |
| [GHSA-x22m-j5qq-j49m](https://github.com/advisories/GHSA-x22m-j5qq-j49m) | HIGH | OpenClaw has two SSRF via sendMediaFeishu and markdown image fetching in Feishu extension | 2026-02-18 |
| [GHSA-rwj8-p9vq-25gv](https://github.com/advisories/GHSA-rwj8-p9vq-25gv) | HIGH | OpenClaw has a LFI in BlueBubbles media path handling | 2026-02-18 |
| [GHSA-4564-pvr2-qq4h](https://github.com/advisories/GHSA-4564-pvr2-qq4h) | HIGH | OpenClaw: Prevent shell injection in macOS keychain credential write | 2026-02-18 |
| [GHSA-gq9c-wg68-gwj2](https://github.com/advisories/GHSA-gq9c-wg68-gwj2) | HIGH | OpenClaw has a path traversal in browser trace/download output paths may allow arbitrary file writes | 2026-02-18 |
| [GHSA-v6c6-vqqg-w888](https://github.com/advisories/GHSA-v6c6-vqqg-w888) | HIGH | OpenClaw affected by potential code execution via unsafe hook module path handling in Gateway | 2026-02-18 |
| [GHSA-w5c7-9qqw-6645](https://github.com/advisories/GHSA-w5c7-9qqw-6645) | HIGH | OpenClaw inter-session prompts could be treated as direct user instructions | 2026-02-18 |
| [GHSA-jqpq-mgvm-f9r6](https://github.com/advisories/GHSA-jqpq-mgvm-f9r6) | HIGH | OpenClaw: Command hijacking via unsafe PATH handling (bootstrapping + node-host PATH overrides) | 2026-02-18 |
| [GHSA-rq6g-px6m-c248](https://github.com/advisories/GHSA-rq6g-px6m-c248) | HIGH | OpenClaw Google Chat shared-path webhook target ambiguity allowed cross-account policy-context misrouting | 2026-02-18 |
| [GHSA-q447-rj3r-2cgh](https://github.com/advisories/GHSA-q447-rj3r-2cgh) | HIGH | OpenClaw affected by denial of service via unbounded webhook request body buffering | 2026-02-18 |
| [GHSA-j27p-hq53-9wgc](https://github.com/advisories/GHSA-j27p-hq53-9wgc) | HIGH | OpenClaw affected by denial of service via unbounded URL-backed media fetch | 2026-02-18 |
| [GHSA-rmxw-jxxx-4cpc](https://github.com/advisories/GHSA-rmxw-jxxx-4cpc) | MEDIUM | OpenClaw has a Matrix allowlist bypass via displayName and cross-homeserver localpart matching | 2026-02-17 |
| [GHSA-mv9j-6xhh-g383](https://github.com/advisories/GHSA-mv9j-6xhh-g383) | MEDIUM | OpenClaw's unauthenticated Nostr profile HTTP endpoints allow remote profile/config tampering | 2026-02-17 |
| [GHSA-wfp2-v9c7-fh79](https://github.com/advisories/GHSA-wfp2-v9c7-fh79) | MEDIUM | OpenClaw affected by SSRF via attachment/media URL hydration | 2026-02-17 |
| [GHSA-xc7w-v5x6-cc87](https://github.com/advisories/GHSA-xc7w-v5x6-cc87) | MEDIUM | OpenClaw has a webhook auth bypass when gateway is behind a reverse proxy (loopback remoteAddress trust) | 2026-02-17 |
| [GHSA-qw99-grcx-4pvm](https://github.com/advisories/GHSA-qw99-grcx-4pvm) | MEDIUM | OpenClaw's Chrome extension relay binds publicly due to wildcard treated as loopback | 2026-02-17 |
| [GHSA-jfv4-h8mc-jcp8](https://github.com/advisories/GHSA-jfv4-h8mc-jcp8) | MEDIUM | OpenClaw: Process Safety - Unvalidated PID Kill via SIGKILL in Process Cleanup | 2026-02-18 |
| [GHSA-7rcp-mxpq-72pj](https://github.com/advisories/GHSA-7rcp-mxpq-72pj) | MEDIUM | OpenClaw Chutes manual OAuth state validation bypass can cause credential substitution | 2026-02-18 |
| [GHSA-5xfq-5mr7-426q](https://github.com/advisories/GHSA-5xfq-5mr7-426q) | MEDIUM | OpenClaw's unsanitized session ID enables path traversal in transcript file operations | 2026-02-18 |
| [GHSA-pg2v-8xwh-qhcc](https://github.com/advisories/GHSA-pg2v-8xwh-qhcc) | MEDIUM | OpenClaw affected by SSRF in optional Tlon (Urbit) extension authentication | 2026-02-18 |
| [GHSA-c37p-4qqg-3p76](https://github.com/advisories/GHSA-c37p-4qqg-3p76) | MEDIUM | OpenClaw Twilio voice-call webhook auth bypass when ngrok loopback compatibility is enabled | 2026-02-18 |
| [GHSA-mj5r-hh7j-4gxf](https://github.com/advisories/GHSA-mj5r-hh7j-4gxf) | MEDIUM | OpenClaw Telegram allowlist authorization accepted mutable usernames | 2026-02-18 |
| [GHSA-h89v-j3x9-8wqj](https://github.com/advisories/GHSA-h89v-j3x9-8wqj) | MEDIUM | OpenClaw affected by denial of service through unguarded archive extraction allowing high expansion/resource abuse (ZIP/TAR) | 2026-02-18 |
| [GHSA-w2cg-vxx6-5xjg](https://github.com/advisories/GHSA-w2cg-vxx6-5xjg) | MEDIUM | OpenClaw: denial of service through large base64 media files allocating large buffers before limit checks | 2026-02-18 |
| [GHSA-v773-r54f-q32w](https://github.com/advisories/GHSA-v773-r54f-q32w) | MEDIUM | OpenClaw Slack: dmPolicy=open allowed any DM sender to run privileged slash commands | 2026-02-18 |
| [GHSA-xvhf-x56f-2hpp](https://github.com/advisories/GHSA-xvhf-x56f-2hpp) | MEDIUM | OpenClaw exec approvals: safeBins could bypass stdin-only constraints via shell expansion | 2026-02-18 |
| [GHSA-chm2-m3w2-wcxm](https://github.com/advisories/GHSA-chm2-m3w2-wcxm) | LOW | OpenClaw Google Chat spoofing access with allowlist authorized mutable email principal despite sender-ID mismatch | 2026-02-17 |
| [GHSA-g27f-9qjv-22pm](https://github.com/advisories/GHSA-g27f-9qjv-22pm) | LOW | OpenClaw log poisoning (indirect prompt injection) via WebSocket headers | 2026-02-17 |
### Repo-Only Advisories (~29 more)

These advisories are listed on the [repo security page](https://github.com/openclaw/openclaw/security/advisories) but lack Advisory DB package mappings:

| GHSA | Severity | Title |
|------|----------|-------|
| [GHSA-gv46-4xfq-jv58](https://github.com/openclaw/openclaw/security/advisories/GHSA-gv46-4xfq-jv58) | **CRITICAL** | RCE via Node Invoke Approval Bypass in Gateway |
| [GHSA-943q-mwmv-hhvh](https://github.com/openclaw/openclaw/security/advisories/GHSA-943q-mwmv-hhvh) | HIGH | Gateway /tools/invoke tool escalation + ACP permission auto-approval |
| [GHSA-rwj8-p9vq-25gv](https://github.com/openclaw/openclaw/security/advisories/GHSA-rwj8-p9vq-25gv) | HIGH | LFI in BlueBubbles media path handling |
| [GHSA-4564-pvr2-qq4h](https://github.com/openclaw/openclaw/security/advisories/GHSA-4564-pvr2-qq4h) | HIGH | Shell injection in macOS keychain credential write |
| [GHSA-x22m-j5qq-j49m](https://github.com/openclaw/openclaw/security/advisories/GHSA-x22m-j5qq-j49m) | HIGH | Two SSRF via sendMediaFeishu and markdown image fetching |
| [GHSA-gq9c-wg68-gwj2](https://github.com/openclaw/openclaw/security/advisories/GHSA-gq9c-wg68-gwj2) | HIGH | Path traversal in browser trace/download output paths |
| [GHSA-h9g4-589h-68xv](https://github.com/openclaw/openclaw/security/advisories/GHSA-h9g4-589h-68xv) | HIGH | Auth bypass in sandbox browser bridge server |
| [GHSA-xw4p-pw82-hqr7](https://github.com/openclaw/openclaw/security/advisories/GHSA-xw4p-pw82-hqr7) | HIGH | Sandbox skill mirroring path traversal |
| [GHSA-v892-hwpg-jwqp](https://github.com/openclaw/openclaw/security/advisories/GHSA-v892-hwpg-jwqp) | HIGH | Path traversal (Zip Slip) in archive extraction |
| [GHSA-qpjj-47vm-64pj](https://github.com/openclaw/openclaw/security/advisories/GHSA-qpjj-47vm-64pj) | HIGH | Missing auth for local browser-control endpoints |
| [GHSA-p25h-9q54-ffvw](https://github.com/openclaw/openclaw/security/advisories/GHSA-p25h-9q54-ffvw) | HIGH | Zip Slip path traversal in tar archive extraction |
| [GHSA-r5h9-vjqc-hq3r](https://github.com/openclaw/openclaw/security/advisories/GHSA-r5h9-vjqc-hq3r) | HIGH | Nextcloud Talk allowlist bypass via displayName spoofing |
| [GHSA-2qj5-gwg2-xwc4](https://github.com/openclaw/openclaw/security/advisories/GHSA-2qj5-gwg2-xwc4) | HIGH | Unsanitized CWD path injection into LLM prompts |
| [GHSA-w235-x559-36mg](https://github.com/openclaw/openclaw/security/advisories/GHSA-w235-x559-36mg) | MODERATE | Docker container escape via unvalidated bind mount config |
| [GHSA-6hf3-mhgc-cm65](https://github.com/openclaw/openclaw/security/advisories/GHSA-6hf3-mhgc-cm65) | HIGH | Session tool visibility hardening and Telegram webhook secret fallback |
| [GHSA-37gc-85xm-2ww6](https://github.com/openclaw/openclaw/security/advisories/GHSA-37gc-85xm-2ww6) | MODERATE | Stored XSS in Control UI via unsanitized assistant name/avatar |
| [GHSA-fh3f-q9qw-93j9](https://github.com/openclaw/openclaw/security/advisories/GHSA-fh3f-q9qw-93j9) | MODERATE | Replace deprecated sandbox hash algorithm |
| [GHSA-xxvh-5hwj-42pp](https://github.com/openclaw/openclaw/security/advisories/GHSA-xxvh-5hwj-42pp) | MODERATE | Sandbox config hash sorted primitive arrays suppressed container recreation |
| [GHSA-h7f7-89mm-pqh6](https://github.com/openclaw/openclaw/security/advisories/GHSA-h7f7-89mm-pqh6) | MODERATE | Harden skill download target directory validation |
| [GHSA-7rcp-mxpq-72pj](https://github.com/openclaw/openclaw/security/advisories/GHSA-7rcp-mxpq-72pj) | MODERATE | Chutes manual OAuth state validation bypass |
| [GHSA-7xhj-55q9-pc3m](https://github.com/openclaw/openclaw/security/advisories/GHSA-7xhj-55q9-pc3m) | MODERATE | Hook transform module path allows traversal |
| [GHSA-jmm5-fvh5-gf4p](https://github.com/openclaw/openclaw/security/advisories/GHSA-jmm5-fvh5-gf4p) | MODERATE | Non-constant-time token comparison in hooks authentication |
| [GHSA-47q7-97xp-m272](https://github.com/openclaw/openclaw/security/advisories/GHSA-47q7-97xp-m272) | MODERATE | Config writes could persist resolved ${VAR} secrets to disk |
| [GHSA-xwjm-j929-xq7c](https://github.com/openclaw/openclaw/security/advisories/GHSA-xwjm-j929-xq7c) | MODERATE | Path Traversal in Browser Download Functionality |
| [GHSA-p536-vvpp-9mc8](https://github.com/openclaw/openclaw/security/advisories/GHSA-p536-vvpp-9mc8) | MODERATE | Web Fetch DoS via unbounded response parsing |
| [GHSA-3m3q-x3gj-f79x](https://github.com/openclaw/openclaw/security/advisories/GHSA-3m3q-x3gj-f79x) | MODERATE | Voice-call plugin webhook verification bypass behind proxy |
| [GHSA-chf7-jq6g-qrwv](https://github.com/openclaw/openclaw/security/advisories/GHSA-chf7-jq6g-qrwv) | MODERATE | Telegram bot token exposure via logs |
| [GHSA-mmpf-jwf4-h3qv](https://github.com/openclaw/openclaw/security/advisories/GHSA-mmpf-jwf4-h3qv) | LOW | Option injection in pre-commit hook can stage ignored files |
| [GHSA-jfv4-h8mc-jcp8](https://github.com/openclaw/openclaw/security/advisories/GHSA-jfv4-h8mc-jcp8) | LOW | Unvalidated PID Kill via SIGKILL in Process Cleanup |

---

## Naming Inconsistencies

| CVE | vendor | product | packageURL | Description Names |
|-----|--------|---------|------------|-------------------|
| CVE-2026-24763 | `clawdbot` | `clawdbot` | — | OpenClaw (formerly Clawdbot) |
| CVE-2026-25253 | `OpenClaw` | `OpenClaw` | `pkg:npm/clawdbot` | OpenClaw / clawdbot / Moltbot |
| CVE-2026-25593 | `openclaw` | `openclaw` | — | OpenClaw |
| CVE-2026-25157 | `openclaw` | `openclaw` | — | OpenClaw |
| CVE-2026-25475 | `openclaw` | `openclaw` | — | OpenClaw |
---

## Vulnerability Categories

| Category | Count | Examples |
|----------|-------|----------|
| **OS Command Injection (CWE-78)** | 14 | PATH injection, SSH command injection, Docker exec, keychain writes |
| **Path Traversal (CWE-22)** | 15 | MEDIA: paths, plugin install, browser downloads, Zip Slip, transcript paths |
| **SSRF** | 6 | Image tool fetch, Feishu extension, attachment/media URLs, IPv6 bypass |
| **Auth Bypass / Missing Auth** | 16 | WebSocket config.apply, webhook verification, browser relay, sandbox bridge |
| **Allowlist Bypass** | 25 | Telegram usernames, Matrix displayName, Slack DM, Twitch, voice-call |
| **Injection (XSS/CSRF/Prompt)** | 14 | XSS in Control UI, prompt injection via Slack/CWD/logs, CSRF |
| **Denial of Service** | 5 | Unbounded media fetch, webhook body buffering, archive expansion |
---

## Data Sources

| Source | URL |
|--------|-----|
| CVE List v5 | [CVEProject/cvelistV5](https://github.com/CVEProject/cvelistV5) |
| GitHub Advisory DB | [github.com/advisories](https://github.com/advisories?query=openclaw) |
| Repo Security Tab | [openclaw/openclaw/security](https://github.com/openclaw/openclaw/security/advisories) |
| CVE Services API | `https://cveawg.mitre.org/api/cve-id/{CVE-ID}` |

---

<sub>This tracker is auto-generated by [`update_readme.py`](update_readme.py). Data files: [`ghsa-advisories.json`](ghsa-advisories.json), [`cves.json`](cves.json), [`cve-pipeline-status.json`](cve-pipeline-status.json)</sub>
