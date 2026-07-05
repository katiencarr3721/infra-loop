# Changelog — infra-loop

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
