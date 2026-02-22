# 📁 OpenClaw — Full Security Advisory List

> Complete listing of all 108 security advisories tracked for [OpenClaw](https://github.com/openclaw/openclaw).
> For the summary dashboard, see the [main README](README.md).

<sub>Last updated: 2026-02-22 08:12 UTC</sub>

---

## GHSAs with CVE IDs (34)

| GHSA | CVE | Severity | Title | Packages | Fixed in | Published |
|------|-----|----------|-------|----------|----------|-----------|
| [GHSA-cxpw-2g23-2vgw](https://github.com/advisories/GHSA-cxpw-2g23-2vgw) | CVE-2026-27576 | ![Medium](https://img.shields.io/badge/MEDIUM-e17055?style=flat-square) | OpenClaw: ACP prompt-size checks missing in local stdio bridge could reduce responsiveness with very large inputs | npm/openclaw | 2026.2.19 | 2026-02-20 |
| [GHSA-w45g-5746-x9fp](https://github.com/advisories/GHSA-w45g-5746-x9fp) | CVE-2026-27488 | ![Medium](https://img.shields.io/badge/MEDIUM-e17055?style=flat-square) | OpenClaw hardened cron webhook delivery against SSRF | npm/openclaw | 2026.2.19 | 2026-02-20 |
| [GHSA-r6h2-5gqq-v5v6](https://github.com/advisories/GHSA-r6h2-5gqq-v5v6) | CVE-2026-27485 | ![Medium](https://img.shields.io/badge/MEDIUM-e17055?style=flat-square) | OpenClaw: Reject symlinks in local skill packaging script | npm/openclaw | 2026.2.19 | 2026-02-20 |
| [GHSA-wh94-p5m6-mr7j](https://github.com/advisories/GHSA-wh94-p5m6-mr7j) | CVE-2026-27484 | ![Low](https://img.shields.io/badge/LOW-fdcb6e?style=flat-square) | OpenClaw Discord moderation authorization used untrusted sender identity in tool-driven flows | npm/openclaw | 2026.2.18 | 2026-02-20 |
| [GHSA-37gc-85xm-2ww6](https://github.com/advisories/GHSA-37gc-85xm-2ww6) | CVE-2026-27009 | ![Medium](https://img.shields.io/badge/MEDIUM-e17055?style=flat-square) | OpenClaw affected by Stored XSS in Control UI via unsanitized assistant name/avatar in inline script injection | npm/openclaw | 2026.2.15 | 2026-02-18 |
| [GHSA-h7f7-89mm-pqh6](https://github.com/advisories/GHSA-h7f7-89mm-pqh6) | CVE-2026-27008 | ![Medium](https://img.shields.io/badge/MEDIUM-e17055?style=flat-square) | OpenClaw hardened the skill download target directory validation | npm/openclaw | 2026.2.15 | 2026-02-18 |
| [GHSA-xxvh-5hwj-42pp](https://github.com/advisories/GHSA-xxvh-5hwj-42pp) | CVE-2026-27007 | ![Medium](https://img.shields.io/badge/MEDIUM-e17055?style=flat-square) | OpenClaw's sandbox config hash sorted primitive arrays and suppressed needed container recreation | npm/openclaw | 2026.2.15 | 2026-02-18 |
| [GHSA-6hf3-mhgc-cm65](https://github.com/advisories/GHSA-6hf3-mhgc-cm65) | CVE-2026-27004 | ![Medium](https://img.shields.io/badge/MEDIUM-e17055?style=flat-square) | OpenClaw session tool visibility hardening and Telegram webhook secret fallback | npm/openclaw | 2026.2.15 | 2026-02-18 |
| [GHSA-chf7-jq6g-qrwv](https://github.com/advisories/GHSA-chf7-jq6g-qrwv) | CVE-2026-27003 | ![Medium](https://img.shields.io/badge/MEDIUM-e17055?style=flat-square) | OpenClaw: Telegram bot token exposure via logs | npm/openclaw | 2026.2.15 | 2026-02-18 |
| [GHSA-w235-x559-36mg](https://github.com/advisories/GHSA-w235-x559-36mg) | CVE-2026-27002 | ![High](https://img.shields.io/badge/HIGH-d63031?style=flat-square) | OpenClaw: Docker container escape via unvalidated bind mount config injection | npm/openclaw | 2026.2.15 | 2026-02-18 |
| [GHSA-2qj5-gwg2-xwc4](https://github.com/advisories/GHSA-2qj5-gwg2-xwc4) | CVE-2026-27001 | ![High](https://img.shields.io/badge/HIGH-d63031?style=flat-square) | OpenClaw: Unsanitized CWD path injection into LLM prompts | npm/openclaw | 2026.2.15 | 2026-02-18 |
| [GHSA-jfv4-h8mc-jcp8](https://github.com/advisories/GHSA-jfv4-h8mc-jcp8) | CVE-2026-27486 | ![Medium](https://img.shields.io/badge/MEDIUM-e17055?style=flat-square) | OpenClaw: Process Safety - Unvalidated PID Kill via SIGKILL in Process Cleanup | npm/openclaw | 2026.2.14 | 2026-02-18 |
| [GHSA-4564-pvr2-qq4h](https://github.com/advisories/GHSA-4564-pvr2-qq4h) | CVE-2026-27487 | ![High](https://img.shields.io/badge/HIGH-d63031?style=flat-square) | OpenClaw: Prevent shell injection in macOS keychain credential write | npm/openclaw | 2026.2.14 | 2026-02-18 |
| [GHSA-xwjm-j929-xq7c](https://github.com/advisories/GHSA-xwjm-j929-xq7c) | CVE-2026-26972 | ![Medium](https://img.shields.io/badge/MEDIUM-e17055?style=flat-square) | OpenClaw has a Path Traversal in Browser Download Functionality | npm/openclaw | 2026.2.13 | 2026-02-18 |
| [GHSA-3fqr-4cg8-h96q](https://github.com/advisories/GHSA-3fqr-4cg8-h96q) | CVE-2026-26317 | ![High](https://img.shields.io/badge/HIGH-d63031?style=flat-square) | OpenClaw affected by cross-site request forgery (CSRF) through loopback browser mutation endpoints | npm/openclaw, npm/clawdbot | 2026.2.14 | 2026-02-18 |
| [GHSA-m7x8-2w3w-pr42](https://github.com/advisories/GHSA-m7x8-2w3w-pr42) | CVE-2026-26323 | ![High](https://img.shields.io/badge/HIGH-d63031?style=flat-square) | OpenClaw has a command injection in maintainer clawtributors updater | npm/openclaw | 2026.2.14 | 2026-02-18 |
| [GHSA-cv7m-c9jx-vg7q](https://github.com/advisories/GHSA-cv7m-c9jx-vg7q) | CVE-2026-26329 | ![High](https://img.shields.io/badge/HIGH-d63031?style=flat-square) | OpenClaw has a path traversal in browser upload allows local file read | npm/openclaw | 2026.2.14 | 2026-02-18 |
| [GHSA-g34w-4xqq-h79m](https://github.com/advisories/GHSA-g34w-4xqq-h79m) | CVE-2026-26328 | ![Medium](https://img.shields.io/badge/MEDIUM-e17055?style=flat-square) | OpenClaw iMessage group allowlist authorization inherited DM pairing-store identities | npm/openclaw, npm/clawdbot | 2026.2.14 | 2026-02-18 |
| [GHSA-pv58-549p-qh99](https://github.com/advisories/GHSA-pv58-549p-qh99) | CVE-2026-26327 | ![High](https://img.shields.io/badge/HIGH-d63031?style=flat-square) | OpenClaw allows unauthenticated discovery TXT records to steer routing and TLS pinning | npm/openclaw | 2026.2.14 | 2026-02-18 |
| [GHSA-8mh7-phf8-xgfm](https://github.com/advisories/GHSA-8mh7-phf8-xgfm) | CVE-2026-26326 | ![Medium](https://img.shields.io/badge/MEDIUM-e17055?style=flat-square) | OpenClaw skills.status could leak secrets to operator.read clients | npm/openclaw | 2026.2.14 | 2026-02-17 |
| [GHSA-h3f9-mjwj-w476](https://github.com/advisories/GHSA-h3f9-mjwj-w476) | CVE-2026-26325 | ![High](https://img.shields.io/badge/HIGH-d63031?style=flat-square) | OpenClaw Node host system.run rawCommand/command mismatch can bypass allowlist/approvals | npm/openclaw | 2026.2.14 | 2026-02-17 |
| [GHSA-jrvc-8ff5-2f9f](https://github.com/advisories/GHSA-jrvc-8ff5-2f9f) | CVE-2026-26324 | ![High](https://img.shields.io/badge/HIGH-d63031?style=flat-square) | OpenClaw has a SSRF guard bypass via full-form IPv4-mapped IPv6 (loopback / metadata reachable) | npm/openclaw | 2026.2.14 | 2026-02-17 |
| [GHSA-g6q9-8fvw-f7rf](https://github.com/advisories/GHSA-g6q9-8fvw-f7rf) | CVE-2026-26322 | ![High](https://img.shields.io/badge/HIGH-d63031?style=flat-square) | OpenClaw Gateway tool allowed unrestricted gatewayUrl override | npm/openclaw | 2026.2.14 | 2026-02-17 |
| [GHSA-8jpq-5h99-ff5r](https://github.com/advisories/GHSA-8jpq-5h99-ff5r) | CVE-2026-26321 | ![High](https://img.shields.io/badge/HIGH-d63031?style=flat-square) | OpenClaw has a local file disclosure via sendMediaFeishu in Feishu extension | npm/openclaw | 2026.2.14 | 2026-02-17 |
| [GHSA-7q2j-c4q5-rm27](https://github.com/advisories/GHSA-7q2j-c4q5-rm27) | CVE-2026-26320 | ![High](https://img.shields.io/badge/HIGH-d63031?style=flat-square) | OpenClaw macOS deep link confirmation truncation can conceal executed agent message | npm/openclaw | 2026.2.14 | 2026-02-17 |
| [GHSA-4hg8-92x6-h2f3](https://github.com/advisories/GHSA-4hg8-92x6-h2f3) | CVE-2026-26319 | ![High](https://img.shields.io/badge/HIGH-d63031?style=flat-square) | OpenClaw is Missing Webhook Authentication in Telnyx Provider Allows Unauthenticated Requests | npm/openclaw | 2026.2.14 | 2026-02-17 |
| [GHSA-pchc-86f6-8758](https://github.com/advisories/GHSA-pchc-86f6-8758) | CVE-2026-26316 | ![High](https://img.shields.io/badge/HIGH-d63031?style=flat-square) | OpenClaw BlueBubbles webhook auth bypass via loopback proxy trust | npm/openclaw, npm/@openclaw/bluebubbles | 2026.2.13 | 2026-02-17 |
| [GHSA-mp5h-m6qj-6292](https://github.com/advisories/GHSA-mp5h-m6qj-6292) | CVE-2026-25474 | ![High](https://img.shields.io/badge/HIGH-d63031?style=flat-square) | OpenClaw has a Telegram webhook request forgery (missing `channels.telegram.webhookSecret`) → auth bypass | npm/openclaw | 2026.2.1 | 2026-02-17 |
| [GHSA-782p-5fr5-7fj8](https://github.com/advisories/GHSA-782p-5fr5-7fj8) | CVE-2026-24764 | ![Low](https://img.shields.io/badge/LOW-fdcb6e?style=flat-square) | OpenClaw Affected by Remote Code Execution via System Prompt Injection in Slack Channel Descriptions | npm/openclaw | 2026.2.3 | 2026-02-17 |
| [GHSA-g55j-c2v4-pjcg](https://github.com/advisories/GHSA-g55j-c2v4-pjcg) | CVE-2026-25593 | ![High](https://img.shields.io/badge/HIGH-d63031?style=flat-square) | OpenClaw vulnerable to Unauthenticated Local RCE via WebSocket config.apply | npm/openclaw | 2026.1.20 | 2026-02-04 |
| [GHSA-r8g4-86fx-92mq](https://github.com/advisories/GHSA-r8g4-86fx-92mq) | CVE-2026-25475 | ![Medium](https://img.shields.io/badge/MEDIUM-e17055?style=flat-square) | OpenClaw Vulnerable to Local File Inclusion via MEDIA: Path Extraction | npm/openclaw | 2026.1.30 | 2026-02-04 |
| [GHSA-q284-4pvr-m585](https://github.com/advisories/GHSA-q284-4pvr-m585) | CVE-2026-25157 | ![High](https://img.shields.io/badge/HIGH-d63031?style=flat-square) | OpenClaw/Clawdbot has OS Command Injection via Project Root Path in sshNodeCommand | npm/clawdbot | 2026.1.29 | 2026-02-02 |
| [GHSA-g8p2-7wf7-98mq](https://github.com/advisories/GHSA-g8p2-7wf7-98mq) | CVE-2026-25253 | ![High](https://img.shields.io/badge/HIGH-d63031?style=flat-square) | OpenClaw/Clawdbot has 1-Click RCE via Authentication Token Exfiltration From gatewayUrl | npm/clawdbot | 2026.1.29 | 2026-02-02 |
| [GHSA-mc68-q9jw-2h3v](https://github.com/advisories/GHSA-mc68-q9jw-2h3v) | CVE-2026-24763 | ![High](https://img.shields.io/badge/HIGH-d63031?style=flat-square) | OpenClaw/Clawdbot Docker Execution has Authenticated Command Injection via PATH Environment Variable | npm/clawdbot | 2026.1.29 | 2026-02-02 |

---

## GHSAs Without CVE — Potential Future CVEs (45)

| GHSA | Severity | Title | CWEs | Fixed in | Published |
|------|----------|-------|------|----------|-----------|
| [GHSA-qrq5-wjgg-rvqw](https://github.com/advisories/GHSA-qrq5-wjgg-rvqw) | ![Critical](https://img.shields.io/badge/CRITICAL-8b0000?style=flat-square) | OpenClaw has a Path Traversal in Plugin Installation | CWE-22 | 2026.2.1 | 2026-02-17 |
| [GHSA-4rj2-gpmh-qq5x](https://github.com/advisories/GHSA-4rj2-gpmh-qq5x) | ![Critical](https://img.shields.io/badge/CRITICAL-8b0000?style=flat-square) | OpenClaw has an inbound allowlist policy bypass in voice-call extension (empty caller ID + suffix matching) | CWE-287 | 2026.2.2 | 2026-02-17 |
| [GHSA-fhvm-j76f-qmjv](https://github.com/advisories/GHSA-fhvm-j76f-qmjv) | ![Critical](https://img.shields.io/badge/CRITICAL-8b0000?style=flat-square) | OpenClaw has a potential access-group authorization bypass if channel type lookup fails | CWE-285 | 2026.2.1 | 2026-02-17 |
| [GHSA-rv39-79c4-7459](https://github.com/advisories/GHSA-rv39-79c4-7459) | ![Critical](https://img.shields.io/badge/CRITICAL-8b0000?style=flat-square) | OpenClaw's gateway connect could skip device identity checks when auth.token was present but not yet validated | CWE-306 | 2026.2.2 | 2026-02-17 |
| [GHSA-r2c6-8jc8-g32w](https://github.com/advisories/GHSA-r2c6-8jc8-g32w) | ![High](https://img.shields.io/badge/HIGH-d63031?style=flat-square) | Duplicate Advisory: 1-Click RCE via Authentication Token Exfiltration From gatewayUrl | CWE-669 | 2026.1.29 | 2026-02-02 |
| [GHSA-mqpw-46fh-299h](https://github.com/advisories/GHSA-mqpw-46fh-299h) | ![High](https://img.shields.io/badge/HIGH-d63031?style=flat-square) | OpenClaw authorization bypass: operator.write can resolve exec approvals via chat.send -> /approve | CWE-269, CWE-863 | 2026.2.2 | 2026-02-17 |
| [GHSA-7vwx-582j-j332](https://github.com/advisories/GHSA-7vwx-582j-j332) | ![High](https://img.shields.io/badge/HIGH-d63031?style=flat-square) | OpenClaw MS Teams inbound attachment downloader leaks bearer tokens to allowlisted suffix domains | CWE-201 | 2026.2.1 | 2026-02-17 |
| [GHSA-33rq-m5x2-fvgf](https://github.com/advisories/GHSA-33rq-m5x2-fvgf) | ![High](https://img.shields.io/badge/HIGH-d63031?style=flat-square) | OpenClaw Twitch allowFrom is not enforced in optional plugin, unauthorized chat users can trigger agent pipeline | CWE-285 | 2026.2.1 | 2026-02-17 |
| [GHSA-56f2-hvwg-5743](https://github.com/advisories/GHSA-56f2-hvwg-5743) | ![High](https://img.shields.io/badge/HIGH-d63031?style=flat-square) | OpenClaw affected by SSRF in Image Tool Remote Fetch | CWE-918 | 2026.2.2 | 2026-02-17 |
| [GHSA-3hcm-ggvf-rch5](https://github.com/advisories/GHSA-3hcm-ggvf-rch5) | ![High](https://img.shields.io/badge/HIGH-d63031?style=flat-square) | OpenClaw has an exec allowlist bypass via command substitution/backticks inside double quotes | CWE-78 | 2026.2.2 | 2026-02-17 |
| [GHSA-mr32-vwc2-5j6h](https://github.com/advisories/GHSA-mr32-vwc2-5j6h) | ![High](https://img.shields.io/badge/HIGH-d63031?style=flat-square) | OpenClaw's Browser Relay /cdp websocket is missing auth which could allow cross-tab cookie access | CWE-306 | 2026.2.1 | 2026-02-17 |
| [GHSA-qj77-c3c8-9c3q](https://github.com/advisories/GHSA-qj77-c3c8-9c3q) | ![High](https://img.shields.io/badge/HIGH-d63031?style=flat-square) | OpenClaw's Windows cmd.exe parsing may bypass exec allowlist/approval gating | CWE-78 | 2026.2.2 | 2026-02-17 |
| [GHSA-64qx-vpxx-mvqf](https://github.com/advisories/GHSA-64qx-vpxx-mvqf) | ![High](https://img.shields.io/badge/HIGH-d63031?style=flat-square) | OpenClaw has an arbitrary transcript path file write via gateway sessionFile | CWE-23, CWE-73, CWE-78, CWE-284 | 2026.2.12 | 2026-02-17 |
| [GHSA-hv93-r4j3-q65f](https://github.com/advisories/GHSA-hv93-r4j3-q65f) | ![High](https://img.shields.io/badge/HIGH-d63031?style=flat-square) | OpenClaw Hook Session Key Override Enables Targeted Cross-Session Routing | CWE-330, CWE-639 | 2026.2.12 | 2026-02-17 |
| [GHSA-h9g4-589h-68xv](https://github.com/advisories/GHSA-h9g4-589h-68xv) | ![High](https://img.shields.io/badge/HIGH-d63031?style=flat-square) | OpenClaw has an authentication bypass in sandbox browser bridge server | CWE-306 | 2026.2.14 | 2026-02-18 |
| [GHSA-x22m-j5qq-j49m](https://github.com/advisories/GHSA-x22m-j5qq-j49m) | ![High](https://img.shields.io/badge/HIGH-d63031?style=flat-square) | OpenClaw has two SSRF via sendMediaFeishu and markdown image fetching in Feishu extension | CWE-918 | 2026.2.14 | 2026-02-18 |
| [GHSA-rwj8-p9vq-25gv](https://github.com/advisories/GHSA-rwj8-p9vq-25gv) | ![High](https://img.shields.io/badge/HIGH-d63031?style=flat-square) | OpenClaw has a LFI in BlueBubbles media path handling | CWE-22 | 2026.2.14 | 2026-02-18 |
| [GHSA-gq9c-wg68-gwj2](https://github.com/advisories/GHSA-gq9c-wg68-gwj2) | ![High](https://img.shields.io/badge/HIGH-d63031?style=flat-square) | OpenClaw has a path traversal in browser trace/download output paths may allow arbitrary file writes | CWE-22 | 2026.2.13 | 2026-02-18 |
| [GHSA-v6c6-vqqg-w888](https://github.com/advisories/GHSA-v6c6-vqqg-w888) | ![High](https://img.shields.io/badge/HIGH-d63031?style=flat-square) | OpenClaw affected by potential code execution via unsafe hook module path handling in Gateway | CWE-22 | 2026.2.14 | 2026-02-18 |
| [GHSA-w5c7-9qqw-6645](https://github.com/advisories/GHSA-w5c7-9qqw-6645) | ![High](https://img.shields.io/badge/HIGH-d63031?style=flat-square) | OpenClaw inter-session prompts could be treated as direct user instructions | CWE-345 | 2026.2.13 | 2026-02-18 |
| [GHSA-jqpq-mgvm-f9r6](https://github.com/advisories/GHSA-jqpq-mgvm-f9r6) | ![High](https://img.shields.io/badge/HIGH-d63031?style=flat-square) | OpenClaw: Command hijacking via unsafe PATH handling (bootstrapping + node-host PATH overrides) | CWE-78, CWE-427, CWE-807 | 2026.2.14 | 2026-02-18 |
| [GHSA-rq6g-px6m-c248](https://github.com/advisories/GHSA-rq6g-px6m-c248) | ![High](https://img.shields.io/badge/HIGH-d63031?style=flat-square) | OpenClaw Google Chat shared-path webhook target ambiguity allowed cross-account policy-context misrouting | CWE-284, CWE-639 | 2026.2.14 | 2026-02-18 |
| [GHSA-q447-rj3r-2cgh](https://github.com/advisories/GHSA-q447-rj3r-2cgh) | ![High](https://img.shields.io/badge/HIGH-d63031?style=flat-square) | OpenClaw affected by denial of service via unbounded webhook request body buffering | CWE-400 | 2026.2.13 | 2026-02-18 |
| [GHSA-j27p-hq53-9wgc](https://github.com/advisories/GHSA-j27p-hq53-9wgc) | ![High](https://img.shields.io/badge/HIGH-d63031?style=flat-square) | OpenClaw affected by denial of service via unbounded URL-backed media fetch | CWE-400 | 2026.2.14 | 2026-02-18 |
| [GHSA-r5fq-947m-xm57](https://github.com/advisories/GHSA-r5fq-947m-xm57) | ![High](https://img.shields.io/badge/HIGH-d63031?style=flat-square) | OpenClaw has a path traversal in apply_patch could write/delete files outside the workspace | CWE-22 | 2026.2.14 | 2026-02-19 |
| [GHSA-rmxw-jxxx-4cpc](https://github.com/advisories/GHSA-rmxw-jxxx-4cpc) | ![Medium](https://img.shields.io/badge/MEDIUM-e17055?style=flat-square) | OpenClaw has a Matrix allowlist bypass via displayName and cross-homeserver localpart matching | CWE-290 | 2026.2.2 | 2026-02-17 |
| [GHSA-mv9j-6xhh-g383](https://github.com/advisories/GHSA-mv9j-6xhh-g383) | ![Medium](https://img.shields.io/badge/MEDIUM-e17055?style=flat-square) | OpenClaw's unauthenticated Nostr profile HTTP endpoints allow remote profile/config tampering | CWE-285, CWE-306 | 2026.2.12 | 2026-02-17 |
| [GHSA-wfp2-v9c7-fh79](https://github.com/advisories/GHSA-wfp2-v9c7-fh79) | ![Medium](https://img.shields.io/badge/MEDIUM-e17055?style=flat-square) | OpenClaw affected by SSRF via attachment/media URL hydration | CWE-918 | 2026.2.2 | 2026-02-17 |
| [GHSA-xc7w-v5x6-cc87](https://github.com/advisories/GHSA-xc7w-v5x6-cc87) | ![Medium](https://img.shields.io/badge/MEDIUM-e17055?style=flat-square) | OpenClaw has a webhook auth bypass when gateway is behind a reverse proxy (loopback remoteAddress trust) | CWE-306 | 2026.2.12 | 2026-02-17 |
| [GHSA-qw99-grcx-4pvm](https://github.com/advisories/GHSA-qw99-grcx-4pvm) | ![Medium](https://img.shields.io/badge/MEDIUM-e17055?style=flat-square) | OpenClaw's Chrome extension relay binds publicly due to wildcard treated as loopback | CWE-284 | 2026.2.12 | 2026-02-17 |
| [GHSA-7rcp-mxpq-72pj](https://github.com/advisories/GHSA-7rcp-mxpq-72pj) | ![Medium](https://img.shields.io/badge/MEDIUM-e17055?style=flat-square) | OpenClaw Chutes manual OAuth state validation bypass can cause credential substitution | CWE-352 | 2026.2.14 | 2026-02-18 |
| [GHSA-5xfq-5mr7-426q](https://github.com/advisories/GHSA-5xfq-5mr7-426q) | ![Medium](https://img.shields.io/badge/MEDIUM-e17055?style=flat-square) | OpenClaw's unsanitized session ID enables path traversal in transcript file operations | CWE-22 | 2026.2.12 | 2026-02-18 |
| [GHSA-pg2v-8xwh-qhcc](https://github.com/advisories/GHSA-pg2v-8xwh-qhcc) | ![Medium](https://img.shields.io/badge/MEDIUM-e17055?style=flat-square) | OpenClaw affected by SSRF in optional Tlon (Urbit) extension authentication | CWE-918 | 2026.2.14 | 2026-02-18 |
| [GHSA-c37p-4qqg-3p76](https://github.com/advisories/GHSA-c37p-4qqg-3p76) | ![Medium](https://img.shields.io/badge/MEDIUM-e17055?style=flat-square) | OpenClaw Twilio voice-call webhook auth bypass when ngrok loopback compatibility is enabled | CWE-306 | 2026.2.14 | 2026-02-18 |
| [GHSA-mj5r-hh7j-4gxf](https://github.com/advisories/GHSA-mj5r-hh7j-4gxf) | ![Medium](https://img.shields.io/badge/MEDIUM-e17055?style=flat-square) | OpenClaw Telegram allowlist authorization accepted mutable usernames | CWE-284, CWE-290 | 2026.2.14 | 2026-02-18 |
| [GHSA-h89v-j3x9-8wqj](https://github.com/advisories/GHSA-h89v-j3x9-8wqj) | ![Medium](https://img.shields.io/badge/MEDIUM-e17055?style=flat-square) | OpenClaw affected by denial of service through unguarded archive extraction allowing high expansion/resource abuse (ZIP/TAR) | CWE-400 | 2026.2.14 | 2026-02-18 |
| [GHSA-w2cg-vxx6-5xjg](https://github.com/advisories/GHSA-w2cg-vxx6-5xjg) | ![Medium](https://img.shields.io/badge/MEDIUM-e17055?style=flat-square) | OpenClaw: denial of service through large base64 media files allocating large buffers before limit checks | CWE-400 | 2026.2.14 | 2026-02-18 |
| [GHSA-v773-r54f-q32w](https://github.com/advisories/GHSA-v773-r54f-q32w) | ![Medium](https://img.shields.io/badge/MEDIUM-e17055?style=flat-square) | OpenClaw Slack: dmPolicy=open allowed any DM sender to run privileged slash commands | CWE-285 | 2026.2.14 | 2026-02-18 |
| [GHSA-xvhf-x56f-2hpp](https://github.com/advisories/GHSA-xvhf-x56f-2hpp) | ![Medium](https://img.shields.io/badge/MEDIUM-e17055?style=flat-square) | OpenClaw exec approvals: safeBins could bypass stdin-only constraints via shell expansion | CWE-78 | 2026.2.14 | 2026-02-18 |
| [GHSA-6c9j-x93c-rw6j](https://github.com/advisories/GHSA-6c9j-x93c-rw6j) | ![Medium](https://img.shields.io/badge/MEDIUM-e17055?style=flat-square) | OpenClaw safeBins file-existence oracle information disclosure | CWE-203 | 2026.2.19 | 2026-02-19 |
| [GHSA-fh3f-q9qw-93j9](https://github.com/advisories/GHSA-fh3f-q9qw-93j9) | ![Medium](https://img.shields.io/badge/MEDIUM-e17055?style=flat-square) | OpenClaw replaced a deprecated sandbox hash algorithm | CWE-328 | 2026.2.15 | 2026-02-19 |
| [GHSA-p536-vvpp-9mc8](https://github.com/advisories/GHSA-p536-vvpp-9mc8) | ![Medium](https://img.shields.io/badge/MEDIUM-e17055?style=flat-square) | OpenClaw has a Web Fetch DoS via unbounded response parsing | CWE-400 | 2026.2.15 | 2026-02-19 |
| [GHSA-chm2-m3w2-wcxm](https://github.com/advisories/GHSA-chm2-m3w2-wcxm) | ![Low](https://img.shields.io/badge/LOW-fdcb6e?style=flat-square) | OpenClaw Google Chat spoofing access with allowlist authorized mutable email principal despite sender-ID mismatch | CWE-290, CWE-863 | 2026.2.14 | 2026-02-17 |
| [GHSA-g27f-9qjv-22pm](https://github.com/advisories/GHSA-g27f-9qjv-22pm) | ![Low](https://img.shields.io/badge/LOW-fdcb6e?style=flat-square) | OpenClaw log poisoning (indirect prompt injection) via WebSocket headers | CWE-117 | 2026.2.13 | 2026-02-17 |
| [GHSA-4685-c5cp-vp95](https://github.com/advisories/GHSA-4685-c5cp-vp95) | ![Low](https://img.shields.io/badge/LOW-fdcb6e?style=flat-square) | OpenClaw safeBins stdin-only bypass via sort output and recursive grep flags | CWE-78, CWE-184 | 2026.2.19 | 2026-02-19 |

---

## Repo-Only Advisories (29)

These advisories are visible on the [repo security page](https://github.com/openclaw/openclaw/security/advisories) but are not indexed in the GitHub Advisory Database (no npm package mapping). They cannot be fetched via the Advisory Database API.

| GHSA | Severity | Title |
|------|----------|-------|
| [GHSA-gv46-4xfq-jv58](https://github.com/openclaw/openclaw/security/advisories/GHSA-gv46-4xfq-jv58) | ![Critical](https://img.shields.io/badge/CRITICAL-8b0000?style=flat-square) | RCE via Node Invoke Approval Bypass in Gateway |
| [GHSA-943q-mwmv-hhvh](https://github.com/openclaw/openclaw/security/advisories/GHSA-943q-mwmv-hhvh) | ![High](https://img.shields.io/badge/HIGH-d63031?style=flat-square) | Gateway /tools/invoke tool escalation + ACP permission auto-approval |
| [GHSA-rwj8-p9vq-25gv](https://github.com/openclaw/openclaw/security/advisories/GHSA-rwj8-p9vq-25gv) | ![High](https://img.shields.io/badge/HIGH-d63031?style=flat-square) | LFI in BlueBubbles media path handling |
| [GHSA-4564-pvr2-qq4h](https://github.com/openclaw/openclaw/security/advisories/GHSA-4564-pvr2-qq4h) | ![High](https://img.shields.io/badge/HIGH-d63031?style=flat-square) | Shell injection in macOS keychain credential write |
| [GHSA-x22m-j5qq-j49m](https://github.com/openclaw/openclaw/security/advisories/GHSA-x22m-j5qq-j49m) | ![High](https://img.shields.io/badge/HIGH-d63031?style=flat-square) | Two SSRF via sendMediaFeishu and markdown image fetching |
| [GHSA-gq9c-wg68-gwj2](https://github.com/openclaw/openclaw/security/advisories/GHSA-gq9c-wg68-gwj2) | ![High](https://img.shields.io/badge/HIGH-d63031?style=flat-square) | Path traversal in browser trace/download output paths |
| [GHSA-h9g4-589h-68xv](https://github.com/openclaw/openclaw/security/advisories/GHSA-h9g4-589h-68xv) | ![High](https://img.shields.io/badge/HIGH-d63031?style=flat-square) | Auth bypass in sandbox browser bridge server |
| [GHSA-xw4p-pw82-hqr7](https://github.com/openclaw/openclaw/security/advisories/GHSA-xw4p-pw82-hqr7) | ![High](https://img.shields.io/badge/HIGH-d63031?style=flat-square) | Sandbox skill mirroring path traversal |
| [GHSA-v892-hwpg-jwqp](https://github.com/openclaw/openclaw/security/advisories/GHSA-v892-hwpg-jwqp) | ![High](https://img.shields.io/badge/HIGH-d63031?style=flat-square) | Path traversal (Zip Slip) in archive extraction |
| [GHSA-qpjj-47vm-64pj](https://github.com/openclaw/openclaw/security/advisories/GHSA-qpjj-47vm-64pj) | ![High](https://img.shields.io/badge/HIGH-d63031?style=flat-square) | Missing auth for local browser-control endpoints |
| [GHSA-p25h-9q54-ffvw](https://github.com/openclaw/openclaw/security/advisories/GHSA-p25h-9q54-ffvw) | ![High](https://img.shields.io/badge/HIGH-d63031?style=flat-square) | Zip Slip path traversal in tar archive extraction |
| [GHSA-r5h9-vjqc-hq3r](https://github.com/openclaw/openclaw/security/advisories/GHSA-r5h9-vjqc-hq3r) | ![High](https://img.shields.io/badge/HIGH-d63031?style=flat-square) | Nextcloud Talk allowlist bypass via displayName spoofing |
| [GHSA-2qj5-gwg2-xwc4](https://github.com/openclaw/openclaw/security/advisories/GHSA-2qj5-gwg2-xwc4) | ![High](https://img.shields.io/badge/HIGH-d63031?style=flat-square) | Unsanitized CWD path injection into LLM prompts |
| [GHSA-w235-x559-36mg](https://github.com/openclaw/openclaw/security/advisories/GHSA-w235-x559-36mg) | ![Medium](https://img.shields.io/badge/MODERATE-e17055?style=flat-square) | Docker container escape via unvalidated bind mount config |
| [GHSA-6hf3-mhgc-cm65](https://github.com/openclaw/openclaw/security/advisories/GHSA-6hf3-mhgc-cm65) | ![High](https://img.shields.io/badge/HIGH-d63031?style=flat-square) | Session tool visibility hardening and Telegram webhook secret fallback |
| [GHSA-37gc-85xm-2ww6](https://github.com/openclaw/openclaw/security/advisories/GHSA-37gc-85xm-2ww6) | ![Medium](https://img.shields.io/badge/MODERATE-e17055?style=flat-square) | Stored XSS in Control UI via unsanitized assistant name/avatar |
| [GHSA-fh3f-q9qw-93j9](https://github.com/openclaw/openclaw/security/advisories/GHSA-fh3f-q9qw-93j9) | ![Medium](https://img.shields.io/badge/MODERATE-e17055?style=flat-square) | Replace deprecated sandbox hash algorithm |
| [GHSA-xxvh-5hwj-42pp](https://github.com/openclaw/openclaw/security/advisories/GHSA-xxvh-5hwj-42pp) | ![Medium](https://img.shields.io/badge/MODERATE-e17055?style=flat-square) | Sandbox config hash sorted primitive arrays suppressed container recreation |
| [GHSA-h7f7-89mm-pqh6](https://github.com/openclaw/openclaw/security/advisories/GHSA-h7f7-89mm-pqh6) | ![Medium](https://img.shields.io/badge/MODERATE-e17055?style=flat-square) | Harden skill download target directory validation |
| [GHSA-7rcp-mxpq-72pj](https://github.com/openclaw/openclaw/security/advisories/GHSA-7rcp-mxpq-72pj) | ![Medium](https://img.shields.io/badge/MODERATE-e17055?style=flat-square) | Chutes manual OAuth state validation bypass |
| [GHSA-7xhj-55q9-pc3m](https://github.com/openclaw/openclaw/security/advisories/GHSA-7xhj-55q9-pc3m) | ![Medium](https://img.shields.io/badge/MODERATE-e17055?style=flat-square) | Hook transform module path allows traversal |
| [GHSA-jmm5-fvh5-gf4p](https://github.com/openclaw/openclaw/security/advisories/GHSA-jmm5-fvh5-gf4p) | ![Medium](https://img.shields.io/badge/MODERATE-e17055?style=flat-square) | Non-constant-time token comparison in hooks authentication |
| [GHSA-47q7-97xp-m272](https://github.com/openclaw/openclaw/security/advisories/GHSA-47q7-97xp-m272) | ![Medium](https://img.shields.io/badge/MODERATE-e17055?style=flat-square) | Config writes could persist resolved ${VAR} secrets to disk |
| [GHSA-xwjm-j929-xq7c](https://github.com/openclaw/openclaw/security/advisories/GHSA-xwjm-j929-xq7c) | ![Medium](https://img.shields.io/badge/MODERATE-e17055?style=flat-square) | Path Traversal in Browser Download Functionality |
| [GHSA-p536-vvpp-9mc8](https://github.com/openclaw/openclaw/security/advisories/GHSA-p536-vvpp-9mc8) | ![Medium](https://img.shields.io/badge/MODERATE-e17055?style=flat-square) | Web Fetch DoS via unbounded response parsing |
| [GHSA-3m3q-x3gj-f79x](https://github.com/openclaw/openclaw/security/advisories/GHSA-3m3q-x3gj-f79x) | ![Medium](https://img.shields.io/badge/MODERATE-e17055?style=flat-square) | Voice-call plugin webhook verification bypass behind proxy |
| [GHSA-chf7-jq6g-qrwv](https://github.com/openclaw/openclaw/security/advisories/GHSA-chf7-jq6g-qrwv) | ![Medium](https://img.shields.io/badge/MODERATE-e17055?style=flat-square) | Telegram bot token exposure via logs |
| [GHSA-mmpf-jwf4-h3qv](https://github.com/openclaw/openclaw/security/advisories/GHSA-mmpf-jwf4-h3qv) | ![Low](https://img.shields.io/badge/LOW-fdcb6e?style=flat-square) | Option injection in pre-commit hook can stage ignored files |
| [GHSA-jfv4-h8mc-jcp8](https://github.com/openclaw/openclaw/security/advisories/GHSA-jfv4-h8mc-jcp8) | ![Low](https://img.shields.io/badge/LOW-fdcb6e?style=flat-square) | Unvalidated PID Kill via SIGKILL in Process Cleanup |

---


## CVE Publication Pipeline Status

| CVE ID | State | In cvelistV5 | GHSA Published | CNA |
|--------|-------|:------------:|----------------|-----|
| CVE-2026-24763 | ✅ **PUBLISHED** | ✅ | 2026-02-02 | GitHub_M |
| CVE-2026-24764 | ✅ **PUBLISHED** | ✅ | 2026-02-17 | GitHub_M |
| CVE-2026-25157 | ✅ **PUBLISHED** | ✅ | 2026-02-02 | GitHub_M |
| CVE-2026-25253 | ✅ **PUBLISHED** | ✅ | 2026-02-02 | mitre |
| CVE-2026-25474 | ✅ **PUBLISHED** | ✅ | 2026-02-17 | GitHub_M |
| CVE-2026-25475 | ✅ **PUBLISHED** | ✅ | 2026-02-04 | GitHub_M |
| CVE-2026-25593 | ✅ **PUBLISHED** | ✅ | 2026-02-04 | GitHub_M |
| CVE-2026-26316 | ✅ **PUBLISHED** | ✅ | 2026-02-17 | GitHub_M |
| CVE-2026-26317 | ✅ **PUBLISHED** | ✅ | 2026-02-18 | GitHub_M |
| CVE-2026-26319 | ✅ **PUBLISHED** | ✅ | 2026-02-17 | GitHub_M |
| CVE-2026-26320 | ✅ **PUBLISHED** | ✅ | 2026-02-17 | GitHub_M |
| CVE-2026-26321 | ✅ **PUBLISHED** | ✅ | 2026-02-17 | GitHub_M |
| CVE-2026-26322 | ✅ **PUBLISHED** | ✅ | 2026-02-17 | GitHub_M |
| CVE-2026-26323 | ✅ **PUBLISHED** | ✅ | 2026-02-18 | GitHub_M |
| CVE-2026-26324 | ✅ **PUBLISHED** | ✅ | 2026-02-17 | GitHub_M |
| CVE-2026-26325 | ✅ **PUBLISHED** | ✅ | 2026-02-17 | GitHub_M |
| CVE-2026-26326 | ✅ **PUBLISHED** | ✅ | 2026-02-17 | GitHub_M |
| CVE-2026-26327 | ✅ **PUBLISHED** | ✅ | 2026-02-18 | GitHub_M |
| CVE-2026-26328 | ✅ **PUBLISHED** | ✅ | 2026-02-18 | GitHub_M |
| CVE-2026-26329 | ✅ **PUBLISHED** | ✅ | 2026-02-18 | GitHub_M |
| CVE-2026-26972 | ✅ **PUBLISHED** | ✅ | 2026-02-18 | GitHub_M |
| CVE-2026-27001 | ✅ **PUBLISHED** | ✅ | 2026-02-18 | GitHub_M |
| CVE-2026-27002 | ✅ **PUBLISHED** | ✅ | 2026-02-18 | GitHub_M |
| CVE-2026-27003 | ✅ **PUBLISHED** | ✅ | 2026-02-18 | GitHub_M |
| CVE-2026-27004 | ✅ **PUBLISHED** | ✅ | 2026-02-18 | GitHub_M |
| CVE-2026-27007 | ✅ **PUBLISHED** | ✅ | 2026-02-18 | GitHub_M |
| CVE-2026-27008 | ✅ **PUBLISHED** | ✅ | 2026-02-18 | GitHub_M |
| CVE-2026-27009 | ✅ **PUBLISHED** | ✅ | 2026-02-18 | GitHub_M |
| CVE-2026-27484 | ✅ **PUBLISHED** | ✅ | 2026-02-20 | GitHub_M |
| CVE-2026-27485 | ✅ **PUBLISHED** | ✅ | 2026-02-20 | GitHub_M |
| CVE-2026-27486 | ✅ **PUBLISHED** | ✅ | 2026-02-18 | GitHub_M |
| CVE-2026-27487 | ✅ **PUBLISHED** | ✅ | 2026-02-18 | GitHub_M |
| CVE-2026-27488 | ✅ **PUBLISHED** | ✅ | 2026-02-20 | GitHub_M |
| CVE-2026-27576 | ✅ **PUBLISHED** | ✅ | 2026-02-20 | GitHub_M |

---

<sub>Auto-generated by <a href="update_readme.py"><code>update_readme.py</code></a> — see <a href="README.md">README.md</a> for the dashboard view.</sub>
