# Deliverable Taxonomy — the menu of artifacts a skill can build

> De-identified, role-agnostic reference. Use it when a backlog idea is tagged `deliverable` to pick an output format and the quality bar to test against. Adapt the categories to the person's actual work.

## The menu

| Category | Format | What it is |
|---|---|---|
| Profiles / snapshots | PPTX | Information-dense 1–6 slide overviews of a company, person, market, or topic |
| Case studies / write-ups | PPTX or DOCX | Documents a completed piece of work via a repeatable template |
| Comparisons / landscapes | XLSX | Comparable-set, peer matrix, option grid, or activity map, source-linked |
| Data packs | XLSX | Multi-tab standardized pulls (metrics, statements, operating data) from sources |
| Models | XLSX | Multi-tab calculations with live formulas and sensitivity (no hardcoded computations) |
| Briefing memos | DOCX (+PDF) | Prose briefing for a meeting, decision, or stakeholder |
| Reports / analyses | DOCX (+PDF) | Longer-form written analysis with cited claims |
| Dashboards | HTML (+XLSX export) | Interactive, filterable view over a compiled dataset; optional refresh schedule |
| Email / newsletter | HTML + .eml | Packages supplied content into a send-ready email |
| In-chat recaps | chat markdown | Recaps/digests delivered in the conversation |

**Output discipline:** Markdown is never a delivered file format (chat only). HTML is labeled "not optimized for print." DOCX and PPTX ship a PDF companion; XLSX does not. File naming: `[Subject]_[Type]_[Date].[ext]`.

## Quality bar by format (what "good" means — test the artifact against this)

- **PPTX** — full information density (the story in ~30s); numbers not adjectives; a source indicator on every data slide + source links in notes; consistent palette + footer; render each slide to an image and check for overlap/cutoff/bleed; PDF companion.
- **XLSX** — formula-driven cells (only verified actuals + assumptions are hardcoded, assumptions visibly flagged); single source of truth per assumption; gridlines off; a Sources tab with clickable links; recalculates with 0 errors; tie/balance checks pass.
- **DOCX/PDF** — native footnotes (no raw `[^x]` markers in Word); every claim sourced with a clickable link; footer = disclaimer + date; PDF companion auto-generated.
- **HTML** — labeled not-for-print; interactive (filters, expandable tables, methodology panel); export to Excel; consistent colors.
- **Email/.eml** — clean template; uses only the content the user supplied (packager, not fabricator); send-ready (drafts only — the human hits send).

## Before building any deliverable skill

Read your org's standards skill (if any) and the relevant output-format helper (xlsx / pptx / docx / pdf) and a brand skill (if any). Write the known-good exemplar first, then build, then self-test the artifact against it with critical gates (not just "did it run").
