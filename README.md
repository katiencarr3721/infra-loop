# infra-loop — v2.0.0

*Builds your AI infrastructure, on a loop.* The name: it builds your AI **infra**structure (a second brain **and** your own skills) via repeating **loop**s — daily capture and weekly synthesis that keep building, reusing, and self-testing your skills and deliverables each cycle. The brain doesn't just store; it scaffolds and improves its own infrastructure every loop.

A shareable, ecosystem-agnostic skill that stands up a self-building "second brain" for one person, end to end: it mines their OWN sources (local AI sessions, email, calendar, chat/IM, cloud files), consolidates them into a canonical wiki of how they think and decide, and sets up daily-capture + weekly-synthesis jobs that keep forging their own skills.

Invoke with **`/infra-loop`**.

## What's in the package
- `SKILL.md` — the deploy-and-run instructions (Phases 0–4).
- `PROMPTS.md` — every parameterized prompt, including the two GLOBAL LINES (injection defense + identifiability) prepended to every agent and job.
- `config_template.md` / `CLAUDE_template.md` — the per-person config and operating manual.
- `CHAT_MINING_PLAYBOOK.md` — the manual web-chat mine (the one source connectors can't reach). Canonical home of the paste-prompts; copied into the brain's `raw/` at scaffold so the reminder always finds it.
- `make_reminder_ics.py` — builds the recurring chat-mining calendar invite. Correct local time in ANY IANA timezone; opens in Outlook, Google Calendar, or Apple Calendar.
- `references/deliverable_taxonomy.md` — generic menu of deliverables + quality bars.
- `SKILL_CRAFT_PRIMER.md` — optional, de-identified "how to build a good skill" starter.
- `build_library.py` — rebuilds the skill-library `index.html`.
- `SELF_TEST.md` — pass/fail gates + test log.
- `CHANGELOG.md` — version history.

## What's new in v2 (highlights)
- **Identifiability is now a choice.** Intake asks whether the person's brain captures real names/clients/figures (default — it's their private working copy) or redacted patterns only. Either way, a hard floor always excludes credentials, government IDs, other people's private data, and personal/health/family content — and anything leaving the brain folder ships redacted.
- **Resumable baseline.** `history/_mining_status.md` tracks every mining agent; interrupted runs resume instead of restarting; agents launch in waves of ≤4.
- **Injection defense** in every prompt that reads mined content.
- **The reminder actually works.** Playbook copied into `raw/`, absolute `.ics` path, correct local time worldwide, Apple Calendar supported, +30-day first reminder if the first pull is skipped.
- **Honest cost estimate** at intake; defined Both/Neither ecosystem paths; numbered job prompts; sample outputs stored as real artifacts.

## Works with Microsoft 365 or Google Workspace (or both, or neither)
Intake asks the ecosystem first and adapts: Outlook/Teams/SharePoint **or** Gmail/Google Chat/Google Drive; "Both" mines each; "Neither" runs on local AI sessions alone. Connectors are discovered at run time, so tool-name changes don't break it. The calendar reminder targets Outlook, Google Calendar, or Apple Calendar.

## Privacy
Each brain is built only from that person's own sources; one person's brain never seeds another's. The skill package itself is de-identified. The only shared element is the optional, de-identified skill-craft primer (generic method, no names/decisions/metrics).

## Supersedes
This is the canonical version of the method. All earlier variants are superseded by infra-loop v2 and can be uninstalled.

License: free to share and adapt.
