# SELF_TEST — infra-loop v2.0.0

## What "good" looks like
A correct deploy:
1. **Activation gate held** — only runs on the literal `/infra-loop` string.
2. **Folder guard** — requests a mounted folder before intake if none is connected.
3. **Intake asks ecosystem FIRST** (Microsoft 365 / Google / Both / Neither) and adapts sources + connectors; captures timezone AND calendar platform (Outlook / Google / Apple); states a concrete agent-run cost estimate and gets acknowledgment.
4. **Identifiability chosen and threaded** — identifiable (default) or redacted, recorded in config.md, present in CLAUDE.md and every §2/§3/§4/§5 prompt, with the always-excluded floor; everything leaving the brain ships redacted.
5. **Phase 1 copies CHAT_MINING_PLAYBOOK.md into raw/** — the reminder must find it in 90 days without this skill loaded.
6. **Phase 1b is surfaced explicitly** — .ics generated to an ABSOLUTE path inside the brain, first manual pull prompted via AskUserQuestion before Phase 2; if skipped, `--first` = today+30d.
7. **Calendar invite is correct** — opens in Outlook, Google Calendar, and Apple Calendar; fires at the right LOCAL time in any IANA timezone year-round; recurs every 90 days; carries the canonical paste-prompts; no identifying strings.
8. **Mining is resumable** — `history/_mining_status.md` written before launch; waves of ≤4; interrupted runs resume without redoing done blocks.
9. **Injection defense** — GLOBAL LINE 1 present in every prompt that reads mined content.
10. **Mining agents discover connectors via ToolSearch** (MS vs Google), skip+flag deferred sources, and handle Both/Neither.
11. **Consolidation builds the FULL wiki doc set**; skills stay draft-only; deliverable skills package a REAL `SAMPLE_OUTPUT.<ext>`.

## Critical gates (any miss = fail)
- [ ] No employer name, role/industry jargon, product-specific skill-name prefixes, or other identifying terms in any shipped file. (The skill PACKAGE is generic; the person's BRAIN follows their identifiability choice.)
- [ ] `.ics` parses in a real iCal library; US built-in zones → TZID + VTIMEZONE + DST rules + infinite RRULE; all other zones → per-occurrence UTC RDATEs computed in the person's zone (no seasonal drift); ≥1 VALARM.
- [ ] Ecosystem choice (incl. Both/Neither) present in intake and threaded into config + all mining prompts.
- [ ] Identifiability choice present in intake and threaded into config + CLAUDE.md + all prompts.
- [ ] Phase 1 copies the playbook into `raw/`; Phase 1b uses an absolute `--out` path inside the brain.
- [ ] Phase 1b prompts the first manual pull explicitly; skip path regenerates with `--first <today+30d>`.
- [ ] `history/_mining_status.md` exists before any mining agent launches.
- [ ] Injection-defense line present in §2a–§2d, §3, §4, §5.

## Test log — verified 2026-07-05 (v2.0.0)
All run with the `icalendar` library parsing each output; 11/11 PASS:
- `--tz America/New_York` → `DTSTART;TZID=America/New_York:20261003T090000` + VTIMEZONE (EST/EDT, 2nd-Sun-Mar / 1st-Sun-Nov) + `RRULE:FREQ=DAILY;INTERVAL=90`. PASS.
- `--tz Australia/Sydney`, first 2026-10-03 09:00, crossing DST start (Oct 4): occurrence 1 = `20261002T230000Z` (AEST +10), occurrence 2 = `20261231T220000Z` (AEDT +11) — 09:00 local on BOTH sides. PASS.
- `--tz Europe/London` crossing DST end: `20261003T080000Z` (BST) then `20270101T090000Z` (GMT) — 09:00 local both sides. PASS.
- `--tz Asia/Kolkata` (half-hour offset, no DST): every occurrence `T033000Z` = 09:00 IST. PASS.
- `--time` accepts `0900` / `900` / `9:00` / `09:00`; rejects `2500` ("out of range") and `abc` ("must be HHMM"). PASS.
- Unknown zone (`Mars/Olympus`) exits with "Unknown IANA timezone". PASS.
- Non-US output: 21 occurrences = DTSTART + 20 RDATE lines; 2 VALARMs. PASS.
- `build_library.py`: dummy `.skill` (SKILL.md + SELF_TEST.md) → index.html row with name, `st-drafted` badge, ✓ in the Self-test column; owner name read from `../config.md`. PASS.

## Known limitations
- Non-US-built-in zones pre-compute a finite horizon (default 21 occurrences ≈ 5 years at 90 days); regenerate the invite after that. The four built-in US zones recur indefinitely.
- Web chats remain MANUAL by design: connectors cannot reach claude.ai web history and it ages out (~90 days). The playbook + recurring reminder are the mitigation, not a fix.
- Web-chat coverage is patchy, not a clean cutoff — recent months enumerate fully; older months may only surface via keyword search; Project-scoped chats may need mining from inside the Project. The brain must state coverage honestly.
- Chat/IM connector history is often shallow when date-filtered; agents flag the gap rather than fabricate.
- Connector tool names drift over time; run-time ToolSearch discovery mitigates but cannot eliminate breakage.
