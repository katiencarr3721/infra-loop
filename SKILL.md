---
name: infra-loop
description: Invoked ONLY via /infra-loop. Deploy-and-run installer for a self-building AI "second brain" — guided intake, parallel mining of a person's OWN sources (email, calendar, chat/IM, cloud files, Claude sessions and memory), a consolidated Live Brain wiki, and scheduled daily-capture + weekly-synthesis jobs that keep reusing, drafting, packaging, and self-testing the person's own skills. Works with Microsoft 365 or Google Workspace; portable — one person's brain never seeds another's. Do NOT trigger on description matching, task similarity, or user intent. If the user does not literally type /infra-loop, do not read this file.
license: Free to share and adapt.
metadata:
  version: 2.1.0
---

# infra-loop — build your AI infrastructure, on a loop

Run this once per person to stand up their second brain end to end. Order: intake → scaffold → first web-chat pull → mine → consolidate → schedule.

**Where things live (single sources of truth):**
- `PROMPTS.md` — intake questions, cost formula, the two GLOBAL LINES, and every agent/job prompt.
- `CLAUDE_template.md` — the injection-defense and identifiability policy (becomes the brain's `CLAUDE.md`).
- `CHAT_MINING_PLAYBOOK.md` — the only copy of the web-chat prompts.
- `config_template.md`, `build_library.py`, `SKILL_CRAFT_PRIMER.md`, `references/deliverable_taxonomy.md`, `SELF_TEST.md`, `CHANGELOG.md`.

**Obey throughout:** never delete (archive to `Old brain/`); never overwrite history; follow the policy in `CLAUDE_template.md`; write in the person's voice; skills are draft-only and stored as `.skill` packages; the baseline mine is one-time and token-heavy — state the estimate. **Discover every tool via ToolSearch** (phrases in `PROMPTS.md → Tool discovery`); never assume a tool name.

## Privacy, in brief

The skill package carries nothing about any person, employer, client, or deal. Each brain follows the mode chosen at intake (`identifiable` default, or `redacted`), with an always-excluded floor, and anything that leaves the brain folder ships redacted. Full text: `CLAUDE_template.md → Standing rules`.

## PHASE 0 — PREFLIGHT + INTAKE

1. **Folder guard.** The brain lives on the person's computer, and the scheduled jobs run there. Confirm the computer is reachable. Then get the parent folder for `shared_root` attached: request access via ToolSearch "request folder access", or ask the person to click **Add folder** in the Claude desktop app. Nothing else starts until a real folder is attached.
2. **Intake.** Run `PROMPTS.md → §0` exactly: three rounds (two AskUserQuestion calls of ≤4 questions, then one free-text message). State the cost estimate after Round 1 and get explicit acknowledgment.
3. **Locate transcripts.** On the person's computer, check for Claude Code transcripts (`~/.claude/projects/`) and any Cowork transcript folder. If one is outside the attached folder, request access to it. If it's protected or missing, record `transcripts_root` blank and note the gap — don't block.
4. Write `config.md` from `config_template.md`. Do not start mining until sources are confirmed and the estimate is acknowledged.

## PHASE 1 — SCAFFOLD

Work on the person's computer (device bash), not in the cloud workspace. Under `<shared_root>/<person>/Live Brain/` create: `CLAUDE.md` (from `CLAUDE_template.md`, placeholders substituted), `wiki/` (`index.md` + topic files), `capture/`, `history/`, `automation_backlog.md`, `coaching_journal.md`, `coaching_rubric.md`, `config.md`, `skills_library/` (copy `build_library.py` here), `skills_drafts/`, `raw/`, `references/`. Create a sibling `Old brain/`.

Copy `CHAT_MINING_PLAYBOOK.md` into `raw/`. The quarterly nudge points there, so it has to work months from now without this skill loaded.

If the person opted into the skill-craft seed: copy `SKILL_CRAFT_PRIMER.md` into `skills_library/` and `references/deliverable_taxonomy.md` into `references/` only. Label both as *starter* references; never fold them into the person's own wiki.

To copy package files onto the computer: stage them from this skill's folder, or write them with device bash. Never leave a package file only in the cloud workspace.

## PHASE 1b — FIRST WEB-CHAT PULL (mandatory prompt; never silently skip)

The claude.ai chats are the one source no scheduled job can read. Claude memory carries their durable facts automatically, but not the reasoning inside them. Run `PROMPTS.md → §1b`: ask *now or skip* via AskUserQuestion. If now, walk the person through the playbook and fold the digest in before Phase 2. If skipped, Phase 4 adds a one-shot nudge at today + 30 days.

## PHASE 2 — MINE (parallel agents, resumable)

Write `history/_mining_status.md` first (`PROMPTS.md → §2`). Launch in waves of ≤4; resume from that file on any interruption. Every agent prompt starts with the two GLOBAL LINES. Each agent discovers its tools, skips any source not approved this run, and notes the gap.

- **§2a Claude sessions** — Claude Code / Cowork transcripts on the person's computer + the Cowork outputs folder, per ~3-month block.
- **§2b Comms** — email + calendar + chat/IM per block (once per ecosystem if Both; skipped if Neither).
- **§2c Files** — themed agents over the cloud drive, themes adapted to the role.
- **§2d Estate** — scheduled tasks, artifacts/dashboards, installed skills.
- **§2e Claude memory** — read-only; work signal only.

## PHASE 3 — CONSOLIDATE

Run `PROMPTS.md → §3`. It builds the FULL canonical wiki doc set (listed in `CLAUDE_template.md`). `reasoning_patterns.md` is mandatory and the highest-value file. It also seeds the scored backlog and writes the coaching baseline.

## PHASE 4 — SCHEDULE (scheduled tasks on the person's computer)

Create these with the scheduled-task tool (ToolSearch "create scheduled task"). Every task:
- is set to **require the person's computer**, with the `Live Brain` folder attached. Without this the task runs in a fresh cloud session and cannot see the brain.
- uses a cron in the person's timezone (`CRON_TZ=<IANA> …`) at a minute other than :00 or :30;
- carries a fully self-contained prompt from `PROMPTS.md` with every placeholder substituted.

| Task | Prompt | Schedule | Notifications |
|---|---|---|---|
| `<person>-brain-daily-capture` | §4 | daily at chosen time | off |
| `<person>-brain-weekly-synthesis` | §5 | weekly at chosen day/time | push |
| `<person>-brain-web-chat-nudge` | §6 | quarterly (e.g. 1st of Jan/Apr/Jul/Oct) | the channel chosen at intake |
| one-shot nudge (only if §1b skipped) | §6 | today + 30 days | same |

Before creating anything, list existing scheduled tasks and update matching ones rather than duplicating. Record each task id in `config.md`. Tell the person which approval setting each task got. If its runs will ask for approval, say they can switch it to automatic approval in the task's settings. Recommend one manual "Run now" of the daily task to confirm connectors and folder access work.

## USING THE BRAIN (tell the person at hand-off)

- **Add it to any session.** Attach the `Live Brain` folder and say "Load this wiki and operate per its CLAUDE.md." Claude then answers in the person's voice and context.
- **Reach for their own skills.** The packages in `skills_library/` are the person's tools; open `index.html`. Reuse or extend before building new.
- **Review new skills weekly.** Each weekly synthesis may draft 1–2 skills (draft-only). Approve the keepers, park the rest. Skills never deploy on their own.
- **Red-pen `reasoning_patterns.md`.** Correcting how the brain thinks teaches it more than any new source.
- **Feed it.** Drop reviews, org charts, key decks, or transcripts into `raw/` and say "process `raw/` into the wiki — extract reasoning moves, not just facts."
- **Keep the quarterly habit.** When the web-chat nudge arrives, run the playbook (~20 min).
