# infra-loop

*Builds your AI infrastructure, on a loop* — a shareable, ecosystem-agnostic skill that stands up a self-building "second brain" AND keeps forging your own skills for one person, end to end. The name: it builds your AI **infra**structure via repeating **loop**s (daily capture + weekly synthesis that build, reuse, and self-test your skills each cycle). It mines a person's OWN sources (local AI sessions, email, calendar, chat/IM, cloud files), consolidates them into a canonical wiki of how they think and decide, and sets up daily-capture + weekly-synthesis jobs that keep building, reusing, and self-testing the person's own skills.

Invoke with **`/infra-loop`**.

## What's in the package
- `SKILL.md` — the deploy-and-run instructions (Phases 0–4).
- `PROMPTS.md` — every parameterized prompt the deploy runs.
- `config_template.md` / `CLAUDE_template.md` — the per-person config and operating manual.
- `CHAT_MINING_PLAYBOOK.md` — the manual web-chat mine (the one source connectors can't reach).
- `make_reminder_ics.py` — builds the recurring 90-day chat-mining calendar invite (Outlook **or** Google Calendar; correct timezone handling).
- `references/deliverable_taxonomy.md` — generic menu of deliverables + quality bars.
- `SKILL_CRAFT_PRIMER.md` — optional, de-identified "how to build a good skill" starter.
- `build_library.py` — rebuilds the skill-library `index.html`.

## Works with Microsoft 365 or Google Workspace
Intake asks the ecosystem first and adapts: Outlook/Teams/SharePoint **or** Gmail/Google Chat/Google Drive. Local AI sessions apply to both. Connectors are discovered at run time, so tool-name changes don't break it. Can add other areas in "Other" if they were you are consistently working/building.

## Privacy
Each brain is built only from that person's own sources; one person's brain never seeds another's. The only shared element is the optional, de-identified skill-craft primer (generic method, no names/decisions/metrics). All persistent files redact confidential/sensitive info.

License: free to share and adapt.
