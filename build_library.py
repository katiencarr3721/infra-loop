#!/usr/bin/env python3
"""
build_library.py - regenerates the skill-library index.

Canonical store: every skill lives here as a `<name>.skill` file (a zip
containing SKILL.md + SELF_TEST.md + SAMPLE_OUTPUT.<ext> + SAMPLE_OUTPUT_NOTES.md).
This script reads each SKILL.md's frontmatter and writes index.html - the
continually-updated list of what each skill does, its status, and its self-test.

Frontmatter it reads (the weekly HANDS step writes exactly this):
    name, description                      top-level
    metadata.status / backlog_id / drafted / version
Top-level status/backlog_id/drafted are also accepted for older packages.

Run it after adding or updating any .skill in this folder:
    python build_library.py [optional/output/index.html]

Portable: the library title comes from the owner's name in ../config.md, so no
identity is hardcoded here. Standard library only.
"""
import sys, os, zipfile, html, datetime, re

LIB = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(LIB, "index.html")
FIELDS = ("status", "backlog_id", "drafted", "version")


def _clean(v):
    v = v.strip()
    if len(v) >= 2 and v[0] == v[-1] and v[0] in "\"'":
        v = v[1:-1]
    return v


def parse_frontmatter(text):
    """Minimal YAML subset: top-level keys, one nested `metadata:` map,
    quoted values, and folded/literal (> or |) multi-line values."""
    m = re.match(r"^﻿?---\s*\r?\n(.*?)\r?\n---\s*(\r?\n|$)", text, re.S)
    fm = {}
    if not m:
        return fm
    lines = m.group(1).splitlines()
    i, parent = 0, None
    while i < len(lines):
        raw = lines[i]
        i += 1
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        indent = len(raw) - len(raw.lstrip())
        if ":" not in raw:
            continue
        k, _, v = raw.strip().partition(":")
        k, v = k.strip(), v.split(" #")[0] if not v.strip().startswith(("'", '"')) else v
        v = v.strip()
        if indent == 0:
            parent = None
        if v in (">", "|", ">-", "|-"):
            block = []
            while i < len(lines) and (not lines[i].strip() or
                                      len(lines[i]) - len(lines[i].lstrip()) > indent):
                block.append(lines[i].strip())
                i += 1
            v = (" " if v.startswith(">") else "\n").join(b for b in block if b)
        elif v == "" and indent == 0:
            parent = k
            fm.setdefault(k, {})
            continue
        if indent > 0 and parent:
            fm[parent][k] = _clean(v)
        else:
            fm[k] = _clean(v)
    meta = fm.get("metadata")
    if isinstance(meta, dict):
        for f in FIELDS:
            if f in meta and f not in fm:
                fm[f] = meta[f]
    return fm


def read_skill(path):
    try:
        with zipfile.ZipFile(path) as z:
            names = z.namelist()
            # Prefer the shallowest SKILL.md (the package root), not one nested in a sample.
            cands = sorted((n for n in names if n.endswith("SKILL.md")), key=lambda n: n.count("/"))
            if not cands:
                return None
            fm = parse_frontmatter(z.read(cands[0]).decode("utf-8", "replace"))
            fm["_has_selftest"] = any(n.endswith("SELF_TEST.md") for n in names)
            fm["_has_sample"] = any(os.path.basename(n).startswith("SAMPLE_OUTPUT.") for n in names)
            return fm
    except zipfile.BadZipFile:
        return None


def owner_name():
    """Read the owner's name from ../config.md; empty string if unavailable."""
    try:
        with open(os.path.join(os.path.dirname(LIB), "config.md"), encoding="utf-8") as cf:
            m = re.search(r"^-?\s*name:\s*(.+)$", cf.read(), re.MULTILINE)
            if m and "{{" not in m.group(1):
                return m.group(1).strip()
    except Exception:
        pass
    return ""


def css_class(status):
    return re.sub(r"[^a-z0-9-]", "", status.lower()) or "draft"


def main():
    skills = []
    for fn in sorted(os.listdir(LIB)):
        if fn.endswith(".skill"):
            fm = read_skill(os.path.join(LIB, fn)) or {}
            fm.setdefault("name", fn[:-6])
            fm["_file"] = fn
            skills.append(fm)

    order = {"shipped": 0, "tested": 1, "drafted": 2, "draft": 2, "idea": 3, "parked": 4}
    skills.sort(key=lambda s: (order.get(str(s.get("status", "draft")).lower(), 9), s.get("name", "")))

    def cell(s, k):
        v = s.get(k, "")
        return html.escape(v if isinstance(v, str) else "")

    rows = []
    for s in skills:
        status = s.get("status", "draft") if isinstance(s.get("status", ""), str) else "draft"
        rows.append(
            "<tr>"
            f"<td class='nm'>{cell(s, 'name')}</td>"
            f"<td><span class='st st-{css_class(status)}'>{html.escape(status)}</span></td>"
            f"<td>{cell(s, 'description')}</td>"
            f"<td class='mono'>{cell(s, 'version')}</td>"
            f"<td>{cell(s, 'backlog_id')}</td>"
            f"<td class='mono'>{cell(s, 'drafted')}</td>"
            f"<td class='mono'>{'&#10003;' if s.get('_has_selftest') else ''}</td>"
            f"<td class='mono'>{'&#10003;' if s.get('_has_sample') else ''}</td>"
            f"<td class='mono'>{cell(s, '_file')}</td>"
            "</tr>"
        )

    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    member = owner_name()
    title = f"Skill Library — {member}" if member else "Skill Library"
    doc = f"""<!doctype html><html><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)}</title>
<style>
:root{{--fg:#1a1a2e;--mut:#666;--line:#e6e6ef;--bg:#fff}}
@media (prefers-color-scheme:dark){{:root{{--fg:#e8e8f0;--mut:#9a9ab0;--line:#2e2e3e;--bg:#14141c}}}}
body{{font:14px/1.5 -apple-system,Segoe UI,Arial,sans-serif;margin:24px;color:var(--fg);background:var(--bg)}}
h1{{font-size:20px;margin:0 0 2px}} .sub{{color:var(--mut);margin:0 0 16px}}
.wrap{{overflow-x:auto}} table{{border-collapse:collapse;width:100%}}
th,td{{text-align:left;padding:8px 10px;border-bottom:1px solid var(--line);vertical-align:top}}
th{{font-size:12px;text-transform:uppercase;letter-spacing:.04em;color:var(--mut)}}
.nm{{font-weight:600;white-space:nowrap}} .mono{{font-family:ui-monospace,Menlo,Consolas,monospace;font-size:12px;white-space:nowrap}}
.st{{font-size:11px;font-weight:600;padding:2px 8px;border-radius:10px}}
.st-shipped{{background:#d6f5e0;color:#0a7a3f}} .st-tested{{background:#dde8ff;color:#1f4fd6}}
.st-drafted,.st-draft{{background:#fff0d6;color:#9a6700}} .st-idea{{background:#eee;color:#555}} .st-parked{{background:#f3d6d6;color:#9a2b2b}}
</style></head><body>
<h1>{html.escape(title)}</h1>
<p class="sub">Auto-generated from the <code>.skill</code> packages in this folder. {len(skills)} skills · last built {now}. Status order: shipped &#8594; tested &#8594; drafted &#8594; idea &#8594; parked.</p>
<div class="wrap"><table><thead><tr><th>Skill</th><th>Status</th><th>What it does</th><th>Ver</th><th>Backlog</th><th>Drafted</th><th>Self-test</th><th>Sample</th><th>File</th></tr></thead>
<tbody>
{os.linesep.join(rows) if rows else '<tr><td colspan="9">No .skill files found.</td></tr>'}
</tbody></table></div>
</body></html>"""

    with open(OUT, "w", encoding="utf-8") as f:
        f.write(doc)
    print(f"Wrote {OUT} ({len(skills)} skills).")


if __name__ == "__main__":
    main()
