# SELF_TEST — infra-loop

## What "good" looks like
A correct deploy:
1. **Activation gate held** — only runs on the literal `/infra-loop` string.
2. **Intake asks ecosystem FIRST** (Microsoft 365 / Google / Both / Neither) and adapts the source picklist and connectors accordingly; captures timezone.
3. **Phase 1b is surfaced explicitly** — the calendar reminder is generated AND the first manual web-chat pull is prompted via AskUserQuestion before Phase 2 (not silently skipped).
4. **Calendar invite is correct** — opens in Outlook or Google Calendar, fires at the right local time, recurs every 90 days, carries the paste-prompts, and contains no identifying strings.
5. **De-identified throughout** — no employer name, role-specific jargon, or product-specific skill names anywhere; redaction language is generic (confidential info, not industry-specific jargon).
6. **Mining agents discover connectors via ToolSearch** (MS vs Google) and skip+flag deferred sources.
7. **Consolidation builds the FULL wiki doc set**; skills stay draft-only.

## Critical gates (any miss = fail)
- [ ] No employer name, role/industry jargon, product-specific skill-name prefixes, single-ecosystem assumptions, or other identifying terms in any shipped file. (Generic only.)
- [ ] Calendar .ics parses in a real iCal library with VTIMEZONE (US) or UTC (non-US), an RRULE, and >=1 VALARM. **Verified 2026-06-28** with the `icalendar` library: US zone → TZID+VTIMEZONE+DST rules; non-US → correct UTC conversion; both parse with RRULE + 2 VALARMs.
- [ ] Ecosystem choice present in intake and threaded into config + all mining prompts.
- [ ] Phase 1b prompts the first manual pull explicitly.

## Calendar-fix test log
- `--tz America/New_York` → `DTSTART;TZID=America/New_York:20260926T090000` + VTIMEZONE (EST/EDT, 2nd-Sun-Mar / 1st-Sun-Nov). PASS.
- `--tz Europe/London` → `DTSTART:20260926T080000Z` (09:00 BST converted to UTC). PASS.
- Both: parsed by `icalendar`, RRULE=FREQ=DAILY;INTERVAL=90, 2 VALARMs. PASS.

## Known limitations
- VTIMEZONE blocks are built-in for the four US zones; other zones use UTC conversion (correct, but the reminder time may drift +-1h across DST — acceptable for a 90-day nudge). Add more VTIMEZONE blocks if precise local time matters outside the US.
- Web chats remain ma