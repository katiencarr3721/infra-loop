# Skill-Craft Primer — how to build a good skill

> Optional, de-identified starter dropped into a person's `skills_library/` only when the operator opts in at intake. It contains NO person-specific content — no names, relationships, decisions, metrics, or economics. It exists for one reason: someone who has never built a skill won't have skill-construction know-how in their own brain yet. Read it when the weekly HANDS pass drafts a skill. Once the person builds real skills, their own library supersedes this.

## What a skill is

A reusable package that turns a repeated piece of work into something Claude can run on demand. Canonical store: a `<name>.skill` zip containing `SKILL.md` (instructions) + `SELF_TEST.md` (how it was validated) + `SAMPLE_OUTPUT.md` (a real produced deliverable). Skills are draft-only until a human approves deployment.

## Reuse before you build (do this FIRST)

Don't reinvent a skill the person can already use. Before drafting anything, inventory what exists:

1. **Org / installed skills** — call `mcp__skills__list_skills` (and `mcp__skills__suggest_skills` for near-matches).
2. **The person's own library** — the `<name>.skill` packages in their `skills_library/` (read `index.html` / the frontmatter).
3. **Shared skills** — any team/shared library at `shared_skills_root` from config, if set.

Then decide in order: **use as-is** (note it in the backlog as "covered by <skill>" and stop); **extend / wrap** (thin variant adding the missing piece); **compose** (chain two skills); **build net-new** (only on a genuine gap — say briefly why nothing fits).

## Stand on foundation skills (build with them, test against them)

Whenever they exist in the person's environment, use them instead of hand-rolling:

- **Standards** — read your org's standards skill (if any) before building; it defines citation, redaction, currency/date/units, file naming, and the validation framework.
- **Brand** — apply your brand skill (if any) for any PPTX / XLSX / HTML output instead of inventing styling.
- **Output-format helpers** — use the `xlsx` / `pptx` / `docx` / `pdf` skills to build the artifact correctly.
- **Reviewer (self-test)** — if a reviewer skill exists, run a finished deliverable through it as part of the self-test; otherwise self-review against your own rubric. Treat findings as gating; fix, don't ship with caveats.

## Pick the right output shape (ask "what does this hand the user?")

- **Deliverable** — the artifact is the point (a deck, a workbook, a model, a memo, a dashboard, an email). Highest felt value. See `references/deliverable_taxonomy.md`.
- **Research** — gathers and synthesizes facts the user then uses.
- **Process** — automates a recurring chore (trackers, reconciliations, hygiene checks, digests).

Tag every backlog idea with one of these. Don't default to "process" — most value is in deliverables.

## Build order (research before formatting)

1. Confirm scope with a short, non-steering intake (data sources: public / upload / both; brand if applicable). Present options equally — never mark one "recommended."
2. Gather every fact/figure first. Do not open the document builder until research is complete.
3. Print an outline with the actual numbers (no placeholders) and align before generating the file.
4. Build, then validate, then package.

## Non-negotiables (the standards that make a skill trustworthy)

- **No fabrication.** Never invent facts, sources, or numbers. If something isn't available, say so plainly ("No public information available"); never round-number guess or gap-fill.
- **Source or cut.** Every claim or URL is verified live before it ships, or it's removed.
- **Redaction.** No confidential/sensitive info in identifiable form (client/deal names, prices, contract terms, secrets, other people's personal data).
- **Single source of truth.** One canonical place per assumption/figure; don't duplicate-and-drift.
- **Human approval before deploy.** Skills stay draft-only until the person approves; nothing auto-sends or auto-deploys.
- **Versioned.** Carry a semantic version + a changelog row; never delete prior versions, archive them.
