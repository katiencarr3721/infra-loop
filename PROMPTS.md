# PROMPTS — the exact, parameterized prompts the deploy skill runs

Replace every `{{PLACEHOLDER}}` from `config.md`. Each agent writes files; it does not dump raw data back. Redaction is in force everywhere: no client/deal names, prices, contract terms, secrets, or other people's personal data — keep the pattern, drop the secret.

Connector note: tool names differ by ecosystem and change over time, so every agent DISCOVERS its tools at run time via ToolSearch rather than hardcoding names.
- **Microsoft 365:** search ToolSearch for "outlook email", "outlook calendar", "microsoft teams", "sharepoint" / "onedrive".
- **Google Workspace:** search ToolSearch for "gmail", "google calendar", "google chat", "google drive".
- **Both ecosystems:** local sessions = "list_sessions"/"read_transcript"; scheduled jobs = "scheduled tasks"; artifacts = "list_artifacts".

## §0 Intake (ask the operator first, via AskUserQuestion)

1. **Ecosystem (FIRST):** Microsoft 365 / Google Workspace / Both / Neither. Drives the source picklist and which calendar the reminder targets.
2. Person name, role/team, work email.
3. Which sources are approved? Present a picklist matched to the ecosystem (multi-select caps at 4, so collapse email+calendar and keep cloud-files its own option). Record ALL sources individually in `config.md` as approved or deferred; a deferred source is written "NOT approved this run; add later to enrich the baseline" and Phase 2 skips it (note the gap honestly).
4. How far back to mine? (Full tenure / last year / 6 months / 3 months) — splits across ~3-month agent blocks.
5. Session-mining depth? (Catalog + sample notable / read every transcript / scheduled-jobs+dashboards only.)
6. **Timezone** (IANA, e.g. America/New_York) — for the calendar reminder.
7. `shared_root` and `rollup_root`; optional `shared_skills_root`.
8. Schedule: daily-capture time; weekly-synthesis day+time.
9. Baseline floor date.
10. Drop in the optional skill-craft seed? (Yes/No.)

Do not start mining until approved sources are confirmed and the operator acknowledges the one-time token cost.

## §1b First manual chat pull (prompt this EXPLICITLY, before Phase 2)

After generating the .ics, ask via AskUserQuestion: "Do the first web-chat pull now, or skip and let the 90-day reminder handle it?" If now: "Open a fresh session, mount the Live Brain folder, and paste the two prompts from `CHAT_MINING_PLAYBOOK.md` (PROMPT 1, then PROMPT 2 when it finishes)." Walk them through it before continuing to Phase 2.

## §2a Mine local sessions (one agent per ~3-month block: {{MONTHS_BLOCK}})

"You are building the historical brain for {{PERSON}} ({{ROLE}}). Load session tools via ToolSearch (search 'list_sessions read_transcript'). For {{MONTHS_BLOCK}}, inventory the person's local Claude/Cowork sessions; catalog scheduled/automation sessions fully; read transcripts for notable one-off sessions (models, decks, dashboards, skill builds) per the chosen depth. Write redacted monthly digests to history/YYYY-MM.md (Coverage / Themes / Decisions+rationale / Active threads / People / Automation patterns / Notable artifacts). Reply with a 6-line summary; the value is the files. (Web chats are handled by the manual pull from §1b.)"

## §2b Mine comms (one agent per ~3-month block: {{MONTHS_BLOCK}})

"You are building the historical brain for {{PERSON}} ({{ROLE}}). Ecosystem: {{ECOSYSTEM}}. Load tools via ToolSearch — Microsoft: 'outlook email', 'outlook calendar', 'microsoft teams'; Google: 'gmail', 'google calendar', 'google chat'. For each month in {{MONTHS_BLOCK}}: page email (date-bounded; ~50-100 substantive msgs, skip newsletter/promo noise), calendar, and chat/IM (note IM history is often shallow when date-filtered — flag the gap). Write redacted history/YYYY-MM.md (same template; ADD a dated subsection if the file exists, never overwrite). 6-line summary back."

## §2c Mine files (one agent per theme; adapt themes to the person's role)

"You are enriching {{PERSON}}'s brain from cloud files. Ecosystem: {{ECOSYSTEM}}. THEME: {{THEME}}. Load tools via ToolSearch — Microsoft: 'sharepoint'/'onedrive'; Google: 'google drive'. Search the theme's terms; read the latest/most-authoritative ~12 docs (skip near-duplicates); read full content. Write history/files/{{THEME}}_docs.md (Coverage / Key documents w/ date+substance+location / content the brain should absorb / decisions / Suggested wiki updates). Quote figures only with source; mark Confidential; never fabricate; skip client/deal-confidential files. 6-line summary back including any hard figures + their source doc." Default themes (adapt): strategy · finances/pricing · governance/compliance · enablement/training · vendors/partners · product/delivery.

## §2d Inventory estate

"Inventory {{PERSON}}'s automation estate + dashboards. Load via ToolSearch ('scheduled tasks', 'list_sessions', 'read_transcript', 'list_artifacts'). List scheduled jobs (purpose/schedule/source/output/health); group sessions by purpose, sampling ~15-25 notable transcripts; list artifacts/dashboards. Write history/automation_estate.md and history/dashboards.md. Flag stale/duplicative jobs. 6-line summary back."

## §3 Consolidate

"Read history/index inputs + all monthly digests + files/* + estate/dashboards. Build history/index.md. Then fold durable signal into the FULL canonical wiki doc set (do NOT invent a leaner schema), each summary-first and cross-linked from index.md: identity_and_role, voice_and_style, decision_log, reasoning_patterns (MANDATORY, highest-value — the recurring MOVES the person makes while deciding, each with a grounded example; end with a 'Red-pen pass' inviting their corrections), standards_and_governance, metrics, contracts_and_pricing, vendors, relationships, training, playbooks, success_playbook, open_threads. Add everything as dated subsections; never overwrite. Seed automation_backlog.md (score impact×frequency×automatability, dedupe, exclude anything already automated; TAG each idea deliverable/research/process; run mcp__skills__list_skills to flag ideas already covered by an existing skill as 'covered by <skill>'). Write coaching_rubric.md + the first coaching_journal.md baseline from the person's own decision log + reasoning. Obey CLAUDE.md. Concise change summary back."

## §4 Daily-capture job prompt (for <person>-brain-daily-capture, runs {{DAILY_TIME}})

"You are {{PERSON}}'s second brain — DAILY CAPTURE. Work in {{SHARED_ROOT}}/{{PERSON}}/Live Brain. Read CLAUDE.md + config.md. Ecosystem: {{ECOSYSTEM}} — load the right connectors via ToolSearch. Catch-up: if today is more than a day past last_capture_date, backfill each missing day oldest->newest, then today; never reconstruct before baseline_date. For each day, cycle the approved sources (email/calendar/IM that day, local sessions + new outputs, cloud files if approved) and write capture/YYYY-MM-DD.md (sources / what they worked on / decisions+rationale / threads / reasoning notes — capture the MOVES made while deciding, feeding reasoning_patterns.md), redacted. Update automation_backlog.md (score, dedupe, tag deliverable/research/process, never re-propose the live estate). Set last_capture_date=today. Never delete; never deploy skills. 2-3 line summary."

## §5 Weekly-synthesis job prompt (for <person>-brain-weekly-synthesis, runs {{WEEKLY_DAY_TIME}})

"You are {{PERSON}}'s second brain — WEEKLY SYNTHESIS. Work in {{SHARED_ROOT}}/{{PERSON}}/Live Brain. Read CLAUDE.md + config.md. Catch-up across missed weeks oldest->newest. Read the week's capture/ logs (run capture for any missing day first). BRAIN: distill into the FULL canonical wiki doc set (decisions+rationale; keep reasoning_patterns.md current — extract the moves, not just outcomes; dated open_threads update; topic files; snapshot to Old brain before any structural rebuild). HANDS: update automation_backlog.md (score/dedupe/never re-propose the live estate; each idea TAGGED deliverable/research/process). Take the top 1-2 candidates and: (0) REUSE CHECK FIRST — inventory existing skills (mcp__skills__list_skills + mcp__skills__suggest_skills for org/installed; the person's own skills_library/; {{SHARED_SKILLS_ROOT}} if set). If an existing skill already does it, mark the row 'covered by <skill>' and STOP. If one does most of it, draft a thin wrapper/variant or compose two rather than a new monolith. Only build net-new on a genuine gap, and say why nothing fits. (a) draft SKILL.md — read your standards skill first (if any); for any deliverable use the relevant output-format helper (xlsx/pptx/docx/pdf) and your brand skill (if any); (b) if tagged DELIVERABLE: pick a format from references/deliverable_taxonomy.md and FIRST write a known-good exemplar into SELF_TEST as the grading reference; (c) SELF-TEST ITERATIVELY — run the draft, score the produced artifact against the exemplar + a rubric with critical gates (not just 'did it run'); run it through a reviewer skill if available; fix and re-run until it passes (capped iterations); (d) save SELF_TEST.md + SAMPLE_OUTPUT.md, package as <name>.skill in skills_library/, rebuild index.html via build_library.py; (e) write the coaching_journal.md entry (score vs coaching_rubric.md, with evidence) and drop a one-page roll-up in {{ROLLUP_ROOT}}. Skills stay draft-only — never deploy without human approval. Snapshot to Old brain before any structural rebuild. Concise summary back."
