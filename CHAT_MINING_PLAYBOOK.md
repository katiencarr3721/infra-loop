# Chat-Mining Playbook (manual, ~20 minutes)

Why this is manual: your **web** chat history (claude.ai and similar) can't be reached by connectors and ages out of retrieval (~90 days). The scheduled jobs capture everything else (email, calendar, chat/IM, cloud files, local sessions) — this is the one source you must pull by hand. Do it now during setup, then every time the 90-day calendar reminder fires.

## How to run

1. Open a fresh Cowork session and mount your `Live Brain` folder.
2. Paste **PROMPT 1**. Let it finish.
3. Paste **PROMPT 2** (the second pass).
4. Paste the **RED-PEN PROMPT** and correct anything that reads wrong — your corrections are the highest-value content in the brain.
5. Save the new wiki version; archive the prior to `../Old brain/` (never delete).

## PROMPT 1 — mine the web chats

```
Load this Live Brain wiki and operate per its CLAUDE.md. I'm going to mine my web chat
history (claude.ai etc.), which connectors can't reach and which ages out ~90 days.

Walk through my web chat history month-by-month, going as far back as it's available.
For each notable chat, extract: what I was working on and why; decisions and the
rationale behind them; HOW I reason (the moves, not just the outcomes); recurring
themes, people (by role, not name), and any automations or artifacts.

Fold the durable signal into the canonical wiki doc set as DATED subsections (especially
reasoning_patterns.md, decision_log.md, open_threads.md). Never overwrite — archive any
prior version to ../Old brain/ first. Redact confidential info (no client/deal names,
prices, contract terms, secrets, or other people's personal data): keep the pattern,
drop the secret. Don't fabricate — if a stretch isn't reachable, say so. End with an
honest coverage statement in open_threads.md and a provenance ledger in
history/<today>_web-chat-backfill.md.
```

## PROMPT 2 — second pass / gap-check

```
Now do a second pass over the same web chat history (and the BACK HALVES of any months
you only sampled — each pull returns ~20 chats). Look specifically for things NOT
already captured: reasoning moves, standards, playbooks, relationships, and open threads
the first pass missed. Add them as dated subsections (don't overwrite; archive priors).
Give me a short summary of what changed and what's still missing.
```

## RED-PEN PROMPT — correct how the brain thinks

```
Show me reasoning_patterns.md. I'll mark corrections inline. Apply my edits, archive the
prior version, and save a new one. Flag any pattern that's thin or inferred from a single
instance so I can confirm or cut it.
```

## Notes
- Coverage is usually patchy, not a clean cutoff: recent months enumerate fully; older months may only be reachable by keyword search; chats inside a Project may need to be mined from inside that Project. Have the brain state this honestly rather than guess.
- Keep personal/sensitive content (health, finances, family, intimate correspondence) OUT of the professional wiki by design.
