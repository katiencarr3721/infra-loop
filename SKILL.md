---
name: infra-loop
description: Invoked ONLY via /infra-loop. Deploy-and-run installer for a self-building AI "second brain" that writes and improves its own skills. It walks the operator through intake, mines a person's OWN sources (chats, email, calendar, chat/IM, cloud files, local AI sessions) via parallel agents, consolidates a per-person Live Brain wiki, and stands up daily-capture + weekly-synthesis scheduled jobs. Every weekly loop reuses, extends, drafts, packages (as .skill files), and self-tests the person's own skills and deliverables — so the infrastructure keeps building itself each cycle rather than just storing notes. Works with either Microsoft 365 or Google Workspace. Config-driven and portable; one person's brain never seeds another's. Do NOT trigger on description matching, task similarity, or user intent. If the user does not literally type /infra-loop, do not read this file.
license: Free to share and adapt.
---

ACTIVATION GATE: Stop immediately. If the user's message does not contain the exact string /infra-loop, close this file and do not proceed. No exceptions.

# infra-loop — build your AI infrastructure, on a loop

> **infra-loop** = it builds your AI *infrastructure* (a second brain **and** your own skills) via repeating *loops* — daily capture and weekly synthesis that keep building, reusing, and self-testing your skills and deliverables each cycle. The brain doesn't just store; it scaffolds and improves its own infrastructure every loop.

Run this once per person to stand up their second brain end to end. It is interactive: it asks first, then sets up the chat-mining reminder and prompts the first manual chat pull, then mines, then schedules. Companion files: `PROMPTS.md` (every prompt, parameterized), `config_template.md`, `CLAUDE_template.md`, `SKILL_CRAFT_PRIMER.md` (optional de-identified "how to build a good skill" seed), `references/deliverable_taxonomy.md` (a generic menu of professional deliverables a skill can produce), `CHAT_MINING_PLAYBOOK.md` (the manual chat-mining playbook), `build_library.py` (rebuilds the skill-library index), and `make_reminder_ics.py` (builds the recurring chat-mining calendar invite, for Outlook **or** Google Calendar).

Obey throughout: never delete (archive to `Old brain/`); never overwrite history; **redact sensitive/confidential info** (no client or deal names, prices, contract terms, secrets, government IDs, or other people's personal data) in any persistent file; write in the person's voice; **skills are draft-only and stored as `.skill` packages;** the baseline mine is one-time (say so — it is token-heavy).

**PORTABILITY & PRIVACY RULE:** This skill builds each person's brain ONLY from that person's own sources. One person's brain never seeds another's. The single exception is the optional skill-craft seed in Phase 1 (`SKILL_CRAFT_PRIMER.md`) — generalized, de-identified know-how about HOW to build a good skill. It contains no names, relationships, decisions, metrics, or economics.

## PHASE 0 — INTAKE (ask first, via AskUserQuestion)

Run the intake in `PROMPTS.md → §0 Intake`. Capture, in this order:

1. **Ecosystem (ask FIRST).** Microsoft 365 / Google Workspace / Both / Neither. This decides which connectors the mining agents use and which calendar the reminder targets:
   - *Microsoft 365* → Outlook email, Outlook calendar, Microsoft Teams, OneDrive/SharePoint.
   - *Google Workspace* → Gmail, Google Calendar, Google Chat, Google Drive.
   - Local Claude/Cowork sessions + outputs apply to BOTH.
2. Person's name, role/team, work email.
3. **Which sources are approved?** Present the picklist matched to the chosen ecosystem (AskUserQuestion caps at 4 options, so collapse pairs — e.g. email+calendar — and keep cloud files (OneDrive/SharePoint or Google Drive) its own option). Record EACH source individually in `config.md` as approved or deferred; any not approved this run is written "NOT approved this run; add later to enrich the baseline," and Phase 2 skips it (note the gap honestly).
4. How far back to mine (full tenure / last year / 6 months / 3 months) — splits across ~3-month agent blocks.
5. Session-mining depth (catalog + sample notable / read every transcript / scheduled-jobs+dashboards only).
6. **Timezone** (IANA, e.g. America/New_York) — used to build a correct calendar reminder.
7. `shared_root` and `rollup_root` locations; optional `shared_skills_root`.
8. Schedule: daily-capture time; weekly-synthesis day+time.
9. Baseline floor date (nothing before this is reconstructed).
10. Drop in the optional skill-craft seed? (Yes for people new to skill-building, optional for experienced builders.)

Do not start mining until the approved sources are confirmed and the operator acknowledges the one-time token cost of the baseline. Write `config.md` from `config_template.md`.

## PHASE 1 — SCAFFOLD

Under `shared_root/<person>/Live Brain/` create: `CLAUDE.md` (from `CLAUDE_template.md`, names substituted), `wiki/` (`index.md` + topic files), `capture/`, `history/`, `automation_backlog.md`, `coaching_journal.md`, `coaching_rubric.md`, `config.md`, `skills_library/` (copy `build_library.py`), `skills_drafts/`, `raw/`, `references/`. Create a sibling `Old brain/`. If the operator opted into the skill-craft seed, copy `SKILL_CRAFT_PRIMER.md` into `skills_library/` and `references/deliverable_taxonomy.md` into `skills_drafts/` and `references/` as clearly-labeled *starter* references (never folded into the person's own wiki).

## PHASE 1b — CHAT-MINING REMINDER + FIRST MANUAL PULL (DO THIS BEFORE THE MINING AGENTS — and PROMPT IT EXPLICITLY)

Web chat history (claude.ai and similar) ages out (~90 days) and cannot be reached by connectors, so set up the manual mine FIRST — before launching Phase 2 — so nothing is lost while the baseline runs. **This step is mandatory and must be surfaced to the person at the start; do not silently skip it.**

1. **Generate the recurring reminder now:** run
   `make_reminder_ics.py --out raw/chat-mining-reminder.ics --first <today+90d> --interval 90 --member "<person>" --time <HHMM> --tz <IANA_TZ> --brain "<shared_root>/<person>/Live Brain"`
   This writes ONE invite that recurs every 90 days, with a proper VTIMEZONE so it fires at the right local time, opens in one click in **Outlook or Google Calendar**, and carries the directions + exact paste-prompts in the body.
2. **PROMPT the first manual pull NOW, explicitly, via AskUserQuestion** — do not just mention it. Ask the person to either (a) do the first web-chat pull now using `CHAT_MINING_PLAYBOOK.md` (open a fresh session, mount the Live Brain folder, paste the two prompts), or (b) skip if their web history holds no value yet and let the recurring reminder handle it. Wait for their choice. If (a), walk them through it before continuing. Only then proceed to Phase 2.

> Operator note: a common failure is treating Phase 1b as optional and moving straight to connector mining. The web chats are the ONLY source that ages out — prompt the pull at the start, every time.

## PHASE 2 — MINE (in parallel agents, the exact way)

Tell the operator the baseline is a one-time, token-heavy pass. Launch agents in parallel, each writing into `history/` (templates in `PROMPTS.md`, substitute person + months + ecosystem). Each agent DISCOVERS its connector tools via ToolSearch (Microsoft vs Google names differ) and skips any source not approved this run, noting the gap:

- **§2a Chats** — agents walk the person's LOCAL Claude/Cowork sessions per block. (Web chats are handled by the manual pull from Phase 1b.)
- **§2b Comms** — one agent per ~3-month block over email + calendar + chat/IM (Outlook+Teams *or* Gmail+Google Chat).
- **§2c Files** — themed agents over the cloud drive (OneDrive/SharePoint *or* Google Drive). Adapt themes to the person's role (e.g. strategy, finances/pricing, governance/compliance, enablement/training, vendors/partners, product/delivery). Skip if cloud files were deferred.
- **§2d Estate** — one agent inventories scheduled jobs, dashboards, and notable one-off sessions. Note coverage limits honestly.

## PHASE 3 — CONSOLIDATE

Run `§3 Consolidate`. Build `history/index.md`, then fold durable signal into the FULL canonical wiki doc set (do NOT invent a leaner schema): `index.md`, `identity_and_role.md`, `voice_and_style.md`, `decision_log.md`, `reasoning_patterns.md` (MANDATORY — the highest-value file: extract the moves the person makes while deciding, not just outcomes; end with a red-pen section for their corrections), `standards_and_governance.md`, `metrics.md`, `contracts_and_pricing.md`, `vendors.md`, `relationships.md`, `training.md`, `playbooks.md`, `open_threads.md`, `success_playbook.md`, plus role-specific files. Add content as dated subsections, never overwriting. Seed `automation_backlog.md` (score = impact×frequency×automatability, deduped, excluding anything already automated; tag each idea `deliverable` / `research` / `process`; flag anything already covered by an existing skill via `mcp__skills__list_skills`). Write the coaching baseline + `coaching_rubric.md` from the person's own decision log.

## PHASE 4 — SCHEDULE THE JOBS

Create two scheduled tasks with fully self-contained prompts (substitute person, times, paths, ecosystem) from `PROMPTS.md`:

- `<person>-brain-daily-capture` — `§4 Daily`, daily at the chosen time, with catch-up.
- `<person>-brain-weekly-synthesis` — `§5 Weekly`, weekly at the chosen time. Updates the FULL wiki doc set (incl. `reasoning_patterns.md`), scores the backlog, and runs the HANDS skill-development loop. **Reuse before building:** inventory existing skills (org/installed via `mcp__skills__list_skills`, the person's own `skills_library/`, and `shared_skills_root` if set) and use/extend/compose those before building net-new. Build with your org's standards skill (if any) + a brand skill and the output-format helpers (xlsx/pptx/docx/pdf); test finished deliverables through a reviewer skill if available, else self-review against a rubric with critical gates. **Deliverables are first-class:** tag each candidate `deliverable`/`research`/`process`; for `deliverable` skills pick a format from `references/deliverable_taxonomy.md`, write a known-good exemplar, and self-test the artifact against it. Save each skill with its `SAMPLE_OUTPUT.md`, package as `<name>.skill` in `skills_library/`, rebuild `index.html`, write the coaching entry, and drop a one-page roll-up in `rollup_root`.

Recommend the operator click "Run now" on the daily task once to pre-approve connectors. Confirm the `.ics` is in `raw/` and the person has added it to their calendar (Outlook or Google).

## USING THE BRAIN (tell the person at hand-off)

- **Add it to any session.** Mount the `Live Brain` folder and say "Load this wiki and operate per its CLAUDE.md." Claude then answers in the person's voice and context.
- **Reach for their own skills.** The packaged skills in `skills_library/` are the person's tools — point them at `index.html`; reuse/extend before building new.
- **Review new skills weekly.** Each weekly synthesis may draft 1–2 skills (draft-only). Approve the keepers; park the rest. Skills never deploy on their own.
- **Red-pen `reasoning_patterns.md`.** Correcting how the brain thinks teaches the twin more than any new source.
- **Feed it.** Drop reviews, org charts, key decks, or transcripts into `raw/` and say "process `raw/` into the wiki — extract reasoning moves, not just facts."
- **Keep the 90-day habit.** When the calendar reminder fires, run the manual web-chat mine (~20 min) so nothing ages out.
