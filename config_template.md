# Config Template — infra-loop (copy per person)

## Person

- name: {{PERSON}}
- role / team: {{ROLE}}
- email: {{EMAIL}}
- tenure / program start (baseline floor): {{BASELINE_FLOOR}}
- timezone (IANA): {{TZ}}   # e.g. America/New_York — used for the calendar reminder

## Ecosystem

- ecosystem: {{ECOSYSTEM}}   # microsoft365 | google | both | neither
  - microsoft365 → Outlook email, Outlook calendar, Microsoft Teams, OneDrive/SharePoint
  - google       → Gmail, Google Calendar, Google Chat, Google Drive
  - Local Claude/Cowork sessions + outputs apply to BOTH.

## Sources to ingest (record each individually as approved or deferred)

A source not approved this run is written "NOT approved this run; add later to enrich the baseline." The baseline still runs on what's approved; deferred sources can be mined later.

- [ ] Local Claude / Cowork sessions
- [ ] Cowork outputs folder
- [ ] Email            (Outlook OR Gmail)
- [ ] Calendar         (Outlook OR Google Calendar)
- [ ] Chat / IM        (Microsoft Teams OR Google Chat)
- [ ] Cloud files      (OneDrive/SharePoint OR Google Drive)   <- keep this its own option; don't let it get squeezed out

## Locations

- shared_root: {{SHARED_ROOT}}        # person Live Brain -> shared_root/{{PERSON}}/Live Brain
- rollup_root: {{ROLLUP_ROOT}}        # weekly one-page roll-up drop
- shared_skills_root: {{SHARED_SKILLS_ROOT}}   # optional team/shared .skill library the HANDS loop scans for reuse; blank if none

## Schedule

- daily_capture: {{DAILY_TIME}} local, every day
- weekly_synthesis: {{WEEKLY_DAY_TIME}} local

## State (updated by the jobs)

- baseline_date: {{BASELINE_FLOOR}}
- last_capture_date: (none yet)
- last_synthesis_date: (none yet)

## Skill-craft seed (portability control)

- include_skill_craft_seed: {{YES_NO}}   # drops the de-identified SKILL_CRAFT_PRIMER.md + references/deliverable_taxonomy.md as a starter. De-identified method only — never another person's content.
