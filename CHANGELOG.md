# Changelog — infra-loop

## 2.1.0 — 2026-10-23

### Fixed
- Scheduled jobs couldn't reach the brain: Phase 4 now creates scheduled tasks that require the person's computer, with the Live Brain folder attached, in the person's timezone, deduplicated against existing tasks, with ids recorded in config.
- Stale hardcoded tool names (folder request, skills listing, session tools) replaced with ToolSearch discovery throughout.
- Skill library index showed blank Status/Backlog/Drafted: the weekly HANDS step now writes a standard `metadata` block, and `build_library.py` reads nested metadata, quoted values, and folded descriptions. Adds Version and Sample columns and dark mode.
- Phase 1b ordering contradiction (generate → ask → regenerate vs ask → generate) removed along with the invite.
- Identifiability wording drifted across six files (e.g. "finances" excluded in one place only). The policy now lives only in `CLAUDE_template.md`, with business vs personal finances made explicit; every other file points to it.

### Changed
- Retired `make_reminder_ics.py` and the `.ics` invite. A quarterly scheduled nudge (push and/or email) replaces it and points at the playbook, so the web-chat prompts now have a single home.
- Web-chat pull now runs in claude.ai (where past-chat search exists); its digest is saved to `raw/` and folded in from Cowork.
- Session mining reads Claude Code / Cowork transcript files on the person's computer instead of assuming session tools.
- Intake regrouped into three rounds that fit AskUserQuestion's 4-question / 4-option limits; calendar-platform question removed; nudge channel added. Questions live only in `PROMPTS.md`.
- Hidden base64/rot13 acknowledgments replaced by a plain Acknowledgments section in README.
- Removed the separate in-body activation gate (the description already carries it); `version` moved under `metadata`.
- README no longer tells users to uninstall earlier variants.

### Added
- §2e: Claude memory as a read-only, work-signal-only source; included in daily capture.
- §6: quarterly web-chat nudge prompt.
- `config.md`: Claude memory and web-chat sources, `transcripts_root`, task ids, `last_web_chat_pull`.
- New SELF_TEST gates: no encoded strings, no hardcoded tool names, single-source checks, scheduled-task reachability.

## 2.0.0 — 2026-07-05

### Fixed
- SELF_TEST.md was truncated mid-sentence; Known Limitations restored and expanded.
- The 90-day reminder pointed at `Live Brain/raw/CHAT_MINING_PLAYBOOK.md` but nothing ever copied the playbook there. Phase 1 now copies it; SELF_TEST gates it.
- Phase 1b `.ics` command used a relative output path that could land the reminder outside the brain; now an absolute path, gated.
- The blanket redaction rule contradicted the wiki schema (contracts_and_pricing.md, metrics.md, relationships.md could never hold real content). Replaced by the two-layer identifiability policy.
- Reminder times now correct in ANY IANA timezone (pre-computed per-occurrence UTC times outside the four built-in US zones), fixing seasonal DST drift worldwide.
- `--time` argument validated (accepts 0900 / 900 / 9:00 / 09:00; rejects garbage).
- build_library.py docstring matched a two-file .skill spec; aligned to the real package contents. Self-test column now shows a check mark; dead code removed.
- PROMPT 1 in the calendar invite had drifted from the playbook's; the playbook is now canonical and both carry the same text.

### Added
- Identifiability intake choice (identifiable default / redacted) threaded through config, CLAUDE.md, and every prompt, with a hard always-excluded floor; everything leaving the brain ships redacted.
- Injection-defense line in every prompt that reads mined content.
- Resumable baseline: `history/_mining_status.md`, waves of ≤4 agents.
- Calendar platform intake (Outlook / Google / Apple).
- Folder-mount guard (step 0) before intake.
- Concrete agent-run cost estimate at intake.
- Defined "Both" and "Neither" ecosystem paths.
- +30-day first reminder when the first manual pull is skipped.
- Numbered daily/weekly job prompts.
- SAMPLE_OUTPUT.<ext> — real artifacts in .skill packages, plus SAMPLE_OUTPUT_NOTES.md.
- Coach spec clarified (≤3 keep / ≤3 work-on, with evidence, trended weekly).
- Semantic version + this changelog.
- New SELF_TEST gates covering all of the above.
- A small debt of gratitude, buried somewhere in the scripts. Happy hunting.

### Changed
- Frontmatter description trimmed (naming rationale moved to README).
- deliverable_taxonomy.md copied to `references/` only (was also skills_drafts/ — single source of truth).
- README notes that infra-loop v2 supersedes all earlier variants of this method.

## 1.0.0
Initial release.
