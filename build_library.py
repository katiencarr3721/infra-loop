#!/usr/bin/env python3
"""
build_library.py — regenerates the skill-library index.

Canonical store: every skill lives here as a `<name>.skill` file (a zip
containing SKILL.md and SELF_TEST.md). This script reads the YAML-ish
frontmatter from each .skill's SKILL.md and writes index.html — the
continually-updated list of what each skill does, is, and its status.

Run it after adding or updating any .skill in this folder:
    python build_library.py
Optional: pass an output path for index.html (default: alongside this file).

Portable: the library title is derived from the owner's name in ../config.md,
so no member identity is hardcoded in this script.
"""
import sys, os, zipfile, html, datetime, re

LIB = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(LIB, "index.html")

FIELDS = ("name", "description", "status", "backlog_id", "drafted")

def parse_frontmatter(text):
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.S)
    fm = {}
    if not m:
        return fm
    for line in m.group(1).splitlines():
        if ":" in line:
            k, _, v = line.partition(":")
            fm[k.strip()] = v.strip()
    return fm

def read_skill(path):
    try:
        with zipfile.ZipFile(path) as z:
            sk = next((n for n in z.namelist() if n.endswith("SKILL.md")), None)
            if not sk:
                return None
            fm = parse_frontmatter(z.read(sk).decode("utf-8", "replace"))
            fm["_has_selftest"] = any(n.endswith("SELF_TEST.md") for n in z.namelist())
            return fm
    except zipfile.BadZipFile:
        return None

def owner_name():
    """Read the member name from ../config.md; empty string if unavailable."""
    try:
        cfg = os.path.join(os.path.dirname(LIB), "config.md")
        with open(cfg, encoding="utf-8") as cf:
            m = re.search(r"^-?\s*name:\s*(.+)$", cf.read(), re.MULTILINE)
            if m:
                return m.group(1).strip()
    except Exception:
        pass
    return ""

def main():
    skills = []
    for fn in sorted(os.listdir(LIB)):
        if fn.endswith(".skill"):
            fm = read_skill(os.path.join(LIB, fn)) or {}
            fm.setdefault("name", fn[:-6])
            fm["_file"] = fn
            skills.append(fm)

    order = {"shipped": 0, "tested": 1, "drafted": 2, "draft": 2, "idea": 3, "parked": 4}
    skills.sort(key=lambda s: (order.get(s.get("status", "draft"), 9), s.get("name", "")))

    rows = []
    for s in skills:
        rows.append(
            "<tr>"
            f"<td class='nm'>{html.escape(s.get('name',''))}</td>"
            f"<td><span class='st st-{html.escape(s.get('status','draft'))}'>{html.escape(s.get('status','draft'))}</span></td>"
            f"<td>{html.escape(s.get('description',''))}</td>"
            f"<td>{html.escape(s.get('backlog_id',''))}</td>"
            f"<td class='mono'>{html.escape(s.get('drafted',''))}</td>"
            f"<td class='mono'>{'v' if s.get('_has_selftest') else ''}</td>"
            f"<td class='mono'>{html.escape(s.get('_file',''))}</td>"
            "</tr>"
        )

    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    member = owner_name()
    title = f"Skill Library — {member}" if member else "Skill Library"
    doc = f"""<!doctype html><html><head><meta charset="utf-8">
<title>{html.escape(title)}</title>
<style>
body{{font:14px/1.5 -apple-system,Segoe UI,Arial,sans-serif;margin:24px;color:#1a1a2e}}
h1{{font-size:20px;margin:0 0 2px}} .sub{{color:#666;margin:0 0 16px}}
table{{border-collapse:collapse;width:100%}} th,td{{text-align:left;padding:8px 10px;border-bottom:1px solid #e6e6ef;vertical-align:top}}
th{{font-size:12px;text-transform:uppercase;letter-spacing:.04em;color:#555}}
.nm{{font-weight:600;white-space:nowrap}} .mono{{font-family:ui-monospace,Menlo,Consolas,monospace;font-size:12px;color:#444;white-space:nowrap}}
.st{{font-size:11px;font-weight:600;padding:2px 8px;border-radius:10px}}
.st-shipped{{background:#d6f5e0;color:#0a7a3f}} .st-tested{{background:#dde8ff;color:#1f4fd6}}
.st-drafted,.st-draft{{background:#fff0d6;color:#9a6700}} .st-idea{{background:#eee;color:#555}} .st-parked{{background:#f3d6d6;color:#9a2b2b}}
</style></head><body>
<h1>{html.escape(title)}</h1>
<p class="sub">Auto-generated from the <code>.skill</code> packages in this folder. {len(skills)} skills · last built {now}. Status order: shipped &#8594; tested &#8594; drafted &#8594; idea &#8594; parked.</p>
<table><thead><tr><th>Skill</th><th>Status</th><th>What it does</th><th>Backlog</th><th>Drafted</th><th>Self-test</th><th>File</th></tr></thead>
<tbody>
{os.linesep.join(rows) if rows else '<tr><td colspan="7">No .skill files found.</td></tr>'}
</tbody></table>
</body></html>"""

    with open(OUT, "w", encoding="utf-8") as f:
        f.write(doc)
    print(f"Wrote {OUT} ({len(skills)} skills).")

if __name__ == "__main__":
    main()
