# Config Template — infra-loop (copy per person)

## Person

- name: {{PERSON}}
- role / team: {{ROLE}}
- email: {{EMAIL}}
- tenure / program start (baseline floor): {{BASELINE_FLOOR}}
- timezone (IANA): {{TZ}}   # e.g. America/New_York — used for every scheduled task

## Ecosystem

- ecosystem: {{ECOSYSTEM}}   # microsoft365 | google | both | neither  (source mapping: PROMPTS.md §0)

## Identifiability

- identifiability: {{IDENTIFIABILITY}}   # identifiable (default) | redacted — policy text lives in CLAUDE.md only

## Sources to ingest (record each individually as approved or deferred)

A source not approved this run is written "NOT approved this run; add later to enrich the baseline." The baseline still runs on what's approved; deferred sources can be mined later.

- [ ] Claude Code / Cowork session transcripts (on this computer)
- [ ] Cowork outputs folder
- [ ] Claude memory (read-only; work signal only)
- [ ] Email            (Outlook OR Gmail)
- [ ] Calendar         (Outlook OR Google Calendar)
- [ ] Chat / IM        (Microsoft Teams OR Google Chat)
- [ ] Cloud files      (OneDrive/SharePoint OR Google Drive)
- [ ] Web chats        (claude.ai — manual, quarterly, via raw/CHAT_MINING_PLAYBOOK.md)

## Locations

- shared_root: {{SHARED_ROOT}}        # Live Brain -> shared_root/{{PERSON}}/Live Brain (absolute path on this computer)
- rollup_root: {{ROLLUP_ROOT}}        # weekly one-page roll-up drop (redacted standard)
- shared_skills_root: {{SHARED_SKILLS_ROOT}}   # optional team/shared .skill library the HANDS loop scans for reuse; blank if none
- transcripts_root: {{TRANSCRIPTS_ROOT}}   # where session transcripts were found (e.g. ~/.claude/projects); blank if unreachable

## Schedule (scheduled tasks — ids recorded so they can be updated, not duplicated)

- daily_capture: {{DAILY_TIME}} local, every day — task id: {{DAILY_TASK_ID}}
- weekly_synthesis: {{WEEKLY_DAY_TIME}} local — task id: {{WEEKLY_TASK_ID}}
- web_chat_nudge: quarterly, {{NUDGE_TIME}} local, via {{NUDGE_CHANNEL}} (push | email | both) — task id: {{NUDGE_TASK_ID}}

## State (updated by the jobs)

- baseline_date: {{BASELINE_FLOOR}}
- last_capture_date: (none yet)
- last_synthesis_date: (none yet)
- last_web_chat_pull: (none yet)
- baseline mining status: see history/_mining_status.md (resume from it if the baseline was interrupted)

## Skill-craft seed (portability control)

- include_skill_craft_seed: {{YES_NO}}   # drops the de-identified SKILL_CRAFT_PRIMER.md + references/deliverable_taxonomy.md as a starter. Generic method only — never another person's content.
