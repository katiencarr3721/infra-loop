#!/usr/bin/env python3
"""
make_reminder_ics.py - generate ONE recurring calendar invite (.ics) that reminds
the person to do the manual chat-mine every 90 days. Works in Outlook AND Google
Calendar.

Why this exists: web chat history (claude.ai and similar) can't be pulled by
connectors and ages out (~90 days). The mine is therefore MANUAL. This invite
carries the directions AND the exact prompts to paste, so the person just opens the
reminder and runs it.

What makes it work correctly across clients (these were the bugs in the prior version):
  * Times are emitted with TZID + a real VTIMEZONE (US zones) or converted to UTC
    (other zones) -- never "floating" local time, which is why reminders used to land
    at the wrong hour or not fire.
  * CRLF line endings and proper 75-octet line folding (RFC 5545).
  * Two VALARMs (at start, and 1 day before) so a reminder actually pops.
  * No identifying PRODID/UID.

Usage:
    python make_reminder_ics.py --out chat-mining-reminder.ics --first 2026-09-24 \
        --interval 90 --member "Name" --time 0900 --tz America/New_York \
        --brain "C:\\...\\Live Brain"
"""
import argparse, datetime, uuid
try:
    from zoneinfo import ZoneInfo
except Exception:  # pragma: no cover
    ZoneInfo = None

PROMPT_1 = (
    'Load this wiki and operate per its CLAUDE.md. Run the chat-mining playbook in '
    'raw/CHAT_MINING_PLAYBOOK.md: page through my web chat history (claude.ai etc.) '
    'month-by-month since the last mining date; flag anything not already in the wiki; '
    'extract HOW I reason (the moves, not just the outcomes); fold it into a NEW wiki '
    'version; never delete (archive priors to ../Old brain/); redact confidential info '
    '(no client/deal names, prices, terms, secrets, or other people\'s personal data); '
    'and write an honest coverage statement in open_threads.md.'
)
PROMPT_2 = (
    'Now page through the BACK HALVES of the months you only sampled (each pull returns '
    '~20 chats), and fold any new findings into another wiki version.'
)

# Built-in correct VTIMEZONE blocks for the common US zones (DST rules baked in).
# Anything not listed falls back to UTC conversion (also correct, may drift +-1h
# seasonally on the reminder time, which is fine for a 90-day nudge).
US_ZONES = {
    "America/New_York": ("EST", "-0500", "EDT", "-0400"),
    "America/Chicago":  ("CST", "-0600", "CDT", "-0500"),
    "America/Denver":   ("MST", "-0700", "MDT", "-0600"),
    "America/Los_Angeles": ("PST", "-0800", "PDT", "-0700"),
}

def vtimezone(tz):
    std, stdoff, dst, dstoff = US_ZONES[tz]
    return [
        "BEGIN:VTIMEZONE", "TZID:" + tz,
        "BEGIN:DAYLIGHT",
        "TZOFFSETFROM:" + stdoff, "TZOFFSETTO:" + dstoff, "TZNAME:" + dst,
        "DTSTART:19700308T020000", "RRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=2SU",
        "END:DAYLIGHT",
        "BEGIN:STANDARD",
        "TZOFFSETFROM:" + dstoff, "TZOFFSETTO:" + stdoff, "TZNAME:" + std,
        "DTSTART:19701101T020000", "RRULE:FREQ=YEARLY;BYMONTH=11;BYDAY=1SU",
        "END:STANDARD",
        "END:VTIMEZONE",
    ]

def build_description(brain):
    parts = [
        "Time to mine your web chats before they age out (~90-day retention).",
        "This is the one step the scheduled jobs cannot do for you - your email,",
        "calendar, chat/IM, cloud files and local sessions are already captured.",
        "",
        "HOW TO RUN (about 20 minutes):",
        "1) Open Cowork and mount your Live Brain folder.",
        "2) The playbook is in Live Brain/raw/CHAT_MINING_PLAYBOOK.md (read it once).",
        "3) Paste PROMPT 1 below. When it finishes, paste PROMPT 2 (the second pass).",
        "4) Red-pen the reasoning_patterns.md it updates - your corrections are the",
        "highest-value content in the whole brain.",
        "5) Save the new version; archive the prior, never delete.",
        "",
        "---- PROMPT 1 (paste into Cowork) ----",
        PROMPT_1,
        "",
        "---- PROMPT 2 (paste after PROMPT 1 finishes) ----",
        PROMPT_2,
        "",
        "Then: 'Red-pen reasoning_patterns.md with my corrections and save a new version.'",
    ]
    if brain:
        parts += ["", "Live Brain: " + brain]
    return "\n".join(parts)

def esc(text):
    return (text.replace("\\", "\\\\").replace(",", "\\,")
                .replace(";", "\\;").replace("\n", "\\n"))

def fold(line):
    out, cur = [], line
    while len(cur.encode("utf-8")) > 75:
        cut = 75
        while len(cur[:cut].encode("utf-8")) > 75:
            cut -= 1
        out.append(cur[:cut]); cur = " " + cur[cut:]
    out.append(cur)
    return "\r\n".join(out)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="chat-mining-reminder.ics")
    ap.add_argument("--first", required=True, help="YYYY-MM-DD first occurrence")
    ap.add_argument("--interval", type=int, default=90)
    ap.add_argument("--member", default="")
    ap.add_argument("--time", default="0900", help="HHMM local")
    ap.add_argument("--tz", default="America/New_York", help="IANA timezone, e.g. America/New_York")
    ap.add_argument("--brain", default="")
    a = ap.parse_args()

    d = datetime.datetime.strptime(a.first, "%Y-%m-%d")
    hh, mm = int(a.time[:2]), int(a.time[2:])
    local_naive = d.replace(hour=hh, minute=mm, second=0)

    use_tzid = a.tz in US_ZONES
    if use_tzid:
        dtstart = "DTSTART;TZID=" + a.tz + ":" + local_naive.strftime("%Y%m%dT%H%M%S")
        dtend = "DTEND;TZID=" + a.tz + ":" + (local_naive + datetime.timedelta(minutes=30)).strftime("%Y%m%dT%H%M%S")
    else:
        # Fallback: convert to UTC so the time is unambiguous everywhere.
        if ZoneInfo is None:
            raise SystemExit("zoneinfo unavailable; use a US zone or install tzdata.")
        aware = local_naive.replace(tzinfo=ZoneInfo(a.tz))
        u = aware.astimezone(datetime.timezone.utc)
        dtstart = "DTSTART:" + u.strftime("%Y%m%dT%H%M%SZ")
        dtend = "DTEND:" + (u + datetime.timedelta(minutes=30)).strftime("%Y%m%dT%H%M%SZ")

    stamp = datetime.datetime.now(datetime.timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    uid = str(uuid.uuid4()) + "@infra-loop"
    summ = "Mine web chats -> second brain" + ((" (" + a.member + ")") if a.member else "")
    desc = build_description(a.brain)

    lines = ["BEGIN:VCALENDAR", "VERSION:2.0",
             "PRODID:-//infra-loop//chat-mining-reminder//EN",
             "CALSCALE:GREGORIAN", "METHOD:PUBLISH"]
    if use_tzid:
        lines += vtimezone(a.tz)
    lines += [
        "BEGIN:VEVENT",
        "UID:" + uid, "DTSTAMP:" + stamp,
        dtstart, dtend,
        "RRULE:FREQ=DAILY;INTERVAL=" + str(a.interval),
        "SUMMARY:" + esc(summ),
        "LOCATION:Cowork - your Live Brain folder",
        "DESCRIPTION:" + esc(desc),
        "BEGIN:VALARM", "ACTION:DISPLAY",
        "DESCRIPTION:Mine your web chats before they age out (~90-day retention)",
        "TRIGGER:PT0S", "END:VALARM",
        "BEGIN:VALARM", "ACTION:DISPLAY",
        "DESCRIPTION:Tomorrow: mine your web chats (manual, ~20 min)",
        "TRIGGER:-P1D", "END:VALARM",
        "END:VEVENT", "END:VCALENDAR",
    ]

    with open(a.out, "w", encoding="utf-8", newline="") as f:
        f.write("\r\n".join(fold(ln) for ln in lines) + "\r\n")
    tzmode = ("TZID " + a.tz) if use_tzid else ("UTC (from " + a.tz + ")")
    print("Wrote " + a.out + " - first " + local_naive.strftime("%Y-%m-%d %H:%M") +
          ", every " + str(a.interval) + " days, recurring; time mode: " + tzmode + ".")

if __name__ == "__main__":
    main()
