# SELF_TEST — infra-loop v2.1.0

## What "good" looks like

A correct deploy:
1. **Activation** — runs only on the literal `/infra-loop` string.
2. **Folder guard** — the person's computer is reachable and a real folder is attached before intake.
3. **Intake follows `PROMPTS.md → §0`** — three rounds; ecosystem first; no AskUserQuestion call exceeds 4 questions or 4 options; concrete cost estimate acknowledged before mining.
4. **Identifiability chosen and threaded** — recorded in `config.md`; full policy appears ONLY in the brain's `CLAUDE.md`; every agent and job prompt carries GLOBAL LINE 2 pointing to it.
5. **Phase 1 copies `CHAT_MINING_PLAYBOOK.md` into `raw/`.**
6. **Phase 1b is surfaced explicitly** — first web-chat pull offered via AskUserQuestion before Phase 2. If skipped, a one-shot nudge is scheduled at today + 30 days.
7. **Mining is resumable** — `history/_mining_status.md` written before launch; waves of ≤4; interrupted runs resume without redoing done blocks.
8. **Injection defense** — GLOBAL LINE 1 in every prompt that reads mined content.
9. **Tools discovered via ToolSearch** — no hardcoded tool names in any prompt; missing sources skipped and flagged.
10. **Claude memory mined read-only, work signal only** — no memory writes; personal content filtered by the floor.
11. **Scheduled tasks can reach the brain** — require the person's computer, have the Live Brain folder attached, use the person's timezone, are deduplicated against existing tasks, and their ids are recorded in `config.md`.
12. **Consolidation builds the FULL wiki doc set**; skills stay draft-only; deliverable skills package a REAL `SAMPLE_OUTPUT.<ext>`; drafted SKILL.md frontmatter carries the `metadata` block `build_library.py` reads.

## Critical gates (any miss = fail)

- [ ] No employer name, person's name, role/industry jargon, or other identifying terms in any shipped file. (Acknowledgments in README are credits to public figures, not user data.)
- [ ] No obfuscated or encoded strings in any shipped file.
- [ ] No hardcoded `mcp__…` tool names in SKILL.md, PROMPTS.md, or SKILL_CRAFT_PRIMER.md.
- [ ] Policy text appears in full only in `CLAUDE_template.md`; other files point to it. (One exception: playbook PROMPT 1 runs in claude.ai, where `CLAUDE.md` can't be loaded, so it carries a one-line version of the floor.)
- [ ] Intake questions appear only in `PROMPTS.md`; web-chat prompts appear only in `CHAT_MINING_PLAYBOOK.md`.
- [ ] Every scheduled task is set to require the person's computer, with the Live Brain folder attached.
- [ ] `history/_mining_status.md` exists before any mining agent launches.
- [ ] Injection-defense line present in §2a–§2e, §3, §4, §5, §6.
- [ ] `build_library.py` renders status / version / backlog / drafted from a §5-format SKILL.md.

## Test log — verified 2026-10-23 (v2.1.0)

`build_library.py`, run against four packages, PASS:
- New-format package (folded `description: >`, nested `metadata` with inline comment and quoted date, SELF_TEST + SAMPLE_OUTPUT.pptx) → row shows `tested`, 0.2.0, B-12, 2026-10-20, ✓ self-test, ✓ sample.
- Old-format package (top-level status/backlog_id/drafted, quoted description containing a colon) → `parked`, B-3, 2026-07-01, colon preserved.
- Package with no frontmatter → falls back to filename, `draft`.
- Corrupt zip → listed by filename, no crash.
- Library title read from `../config.md` ("Skill Library — <name>"); an unfilled `{{PERSON}}` placeholder is ignored.

Static checks, PASS: no `mcp__` names in SKILL.md / PROMPTS.md / primer; GLOBAL LINE 1 in §2a–§2e, §3–§6; cost examples recomputed (last year: 4 blocks × 2 + 6 + 3 = 17; 5 years: 20 × 2 + 9 = 49).

## Known limitations

- claude.ai web chats can't be read by any scheduled job. Memory carries their durable facts automatically; the reasoning detail needs the quarterly manual pull.
- Session transcripts are read from files on the person's computer. Cowork's own transcript location may be protected from the device shell; when it is, the brain says so and relies on outputs, memory, and the estate inventory instead.
- Scheduled tasks run only while the person's computer is on with the Claude desktop app running. Catch-up logic backfills missed days.
- Chat/IM connector history is often shallow when date-filtered; agents flag the gap rather than fabricate.
- Connector tool names drift; run-time ToolSearch discovery mitigates but can't eliminate breakage.
