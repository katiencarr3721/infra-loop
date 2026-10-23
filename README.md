# infra-loop — v2.1.0

*Builds your AI infrastructure, on a loop.* It builds your AI **infra**structure (a second brain **and** your own skills) through repeating **loop**s: daily capture and weekly synthesis that keep building, reusing, and self-testing your skills and deliverables each cycle. The brain doesn't just store; it improves its own infrastructure every loop.

A shareable, ecosystem-agnostic skill that stands up a self-building "second brain" for one person, end to end. It mines their OWN sources (email, calendar, chat/IM, cloud files, Claude sessions, Claude memory), consolidates them into a canonical wiki of how they think and decide, and schedules daily-capture and weekly-synthesis jobs that keep building their own skills.

Invoke with **`/infra-loop`**.

## What's in the package

| File | Role | Single source of truth for |
|---|---|---|
| `SKILL.md` | Deploy-and-run instructions (Phases 0–4) | phase order |
| `PROMPTS.md` | Every parameterized prompt | intake questions, cost formula, GLOBAL LINES, agent + job prompts |
| `CLAUDE_template.md` | The brain's operating manual | injection-defense + identifiability policy, wiki schema |
| `config_template.md` | Per-person config | sources, locations, schedule, state |
| `CHAT_MINING_PLAYBOOK.md` | Manual quarterly web-chat pull | the web-chat prompts |
| `build_library.py` | Rebuilds the skill-library `index.html` | — |
| `SKILL_CRAFT_PRIMER.md` | Optional, de-identified skill-building starter | — |
| `references/deliverable_taxonomy.md` | Deliverable menu + quality bars | — |
| `SELF_TEST.md` | Pass/fail gates + test log | — |
| `CHANGELOG.md` | Version history | — |

## What's new in v2.1

- **Jobs run where the brain lives.** Daily, weekly, and quarterly jobs are scheduled tasks set to require your computer, with the Live Brain folder attached, so they can actually read and write it.
- **The calendar file is gone.** A quarterly scheduled nudge (phone push and/or email) replaces the `.ics` invite and its script. The nudge points at the playbook instead of copying the prompts.
- **More sources mined automatically.** Claude Code / Cowork session transcripts on your computer, and Claude memory (read-only, work signal only), which carries durable facts from your claude.ai chats.
- **The web-chat pull runs where it can work.** It happens in claude.ai, which has past-chat search, and the digest is folded in from Cowork.
- **One home for everything.** Policy, intake, and prompts each live in exactly one file.
- **Intake in three rounds** to fit AskUserQuestion's limits.
- **Skill library index works.** Drafted skills carry `metadata.status / backlog_id / drafted / version`, which `build_library.py` reads.
- **No hardcoded tool names.** Every tool is discovered with ToolSearch.

## Works with Microsoft 365 or Google Workspace (or both, or neither)

Intake asks the ecosystem first and adapts: Outlook/Teams/SharePoint **or** Gmail/Google Chat/Google Drive. "Both" mines each; "Neither" runs on Claude sources alone. Connectors are discovered at run time, so tool-name changes don't break it.

## Privacy

Each brain is built only from that person's own sources; one person's brain never seeds another's. The skill package itself is de-identified. Within a brain, the person chooses `identifiable` (default) or `redacted`. An always-excluded floor applies either way (credentials, ID numbers, other people's private data, and their own personal life), and anything that leaves the brain folder ships redacted. Full policy: `CLAUDE_template.md`.

## Acknowledgments

The second-brain idea owes a debt to Andrej Karpathy. The loop owes one to Boris Cherny. Thank you both.

License: free to share and adapt.
