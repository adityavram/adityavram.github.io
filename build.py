#!/usr/bin/env python3
"""Build a minimal, agent-first personal site from notes/*.md.

Zero dependencies (Python 3 stdlib only). Reads markdown notes with a
simple YAML-ish frontmatter block and writes a static site to docs/:

  notes/<slug>.md     raw markdown  (the canonical agent-readable artifact)
  notes/<slug>.html   minimal HTML render
  index.html          listing
  notes/index.json    machine-readable manifest
  llms.txt            agent index        (llmstxt.org v2)
  llms-full.txt       all notes concatenated, grep-able
  feed.xml            Atom feed
  sitemap.xml
  robots.txt
  .well-known/agent.json
  .nojekyll           tells GitHub Pages to skip Jekyll and serve as-is

Frontmatter format (optional, but recommended):

  ---
  title: Note Title
  date: 2026-11-23
  tags: [ml, scaling]
  status: public          # anything other than "public" is skipped from output
  ---

  Markdown body...

Configure SITE_* constants below, then:  python3 build.py
"""

import json
import re
import html
import datetime
from pathlib import Path
from html import escape

ROOT = Path(__file__).parent
SRC = ROOT / "notes"
OUT = ROOT / "docs"

# --- Configure these -------------------------------------------------------
SITE_TITLE = "Adi Ram — notes"
SITE_AUTHOR = "Adi Ram"
SITE_URL = "https://adityavram.github.io"      # change if you use a custom domain
DESCRIPTION = (
    "Minor notes on things I find interesting, and my own research. "
    "Written for agents first, humans second."
)
# ---------------------------------------------------------------------------


def parse_frontmatter(text):
    """Return (meta dict, body str). Simple key: value + [list] parsing."""
    if text.startswith("---\n"):
        end = text.find("\n---\n", 4)
        if end != -1:
            fm = text[4:end]
            body = text[end + 5 :]
            meta = {}
            for line in fm.splitlines():
                if not line.strip() or line.strip().startswith("#"):
                    continue
                if ":" not in line:
                    continue
                k, v = line.split(":", 1)
                k, v = k.strip(), v.strip()
                if v.startswith("[") and v.endswith("]"):
                    inner = v[1:-1]
                    v = [x.strip().strip("\"'") for x in inner.split(",") if x.strip()]
                elif v.startswith('"') and v.endswith('"'):
                    v = v[1:-1]
                meta[k] = v
            return meta, body
    return {}, text


def md_to_html(md):
    """Pragmatic minimal markdown -> HTML. Handles headings, paragraphs,
    fenced code, links, inline code, bold. Not a full spec — just notes."""
    lines = md.split("\n")
    out = []
    in_code = False
    para = []

    def flush():
        if para:
            out.append("<p>" + " ".join(para) + "</p>")
            para.clear()

    for line in lines:
        if line.strip().startswith("```"):
            if in_code:
                out.append("</code></pre>")
                in_code = False
            else:
                flush()
                out.append("<pre><code>")
                in_code = True
            continue
        if in_code:
            out.append(escape(line))
            continue
        if line.startswith("### "):
            flush()
            out.append(f"<h3>{escape(line[4:])}</h3>")
            continue
        if line.startswith("## "):
            flush()
            out.append(f"<h2>{escape(line[3:])}</h2>")
            continue
        if line.startswith("# "):
            flush()
            out.append(f"<h2>{escape(line[2:])}</h2>")
            continue
        if line.startswith("- ") or line.startswith("* "):
            flush()
            out.append(f"<li>{inline(line[2:])}</li>")
            continue
        if line.strip() == "":
            flush()
            continue
        para.append(inline(line))
    flush()
    if in_code:
        out.append("</code></pre>")
    return "\n".join(out)


def inline(text):
    t = escape(text)
    t = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', t)
    t = re.sub(r"`([^`]+)`", r"<code>\1</code>", t)
    t = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", t)
    return t


PAGE_CSS = """
body{max-width:70ch;margin:2rem auto;padding:0 1rem;
  font:15px/1.6 ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;
  color:#111;background:#fff}
a{color:#111;text-decoration:underline;text-underline-offset:2px}
a:hover{background:#111;color:#fff;text-decoration:none}
h1{font-size:1.2rem;font-weight:600;margin:0 0 1rem}
h2{font-size:1.05rem;font-weight:600;margin:1.6rem 0 .6rem}
h3{font-size:1rem;font-weight:600;margin:1.2rem 0 .4rem}
p,li{margin:.4rem 0}
pre{background:#f4f4f4;padding:.8rem;overflow-x:auto;font-size:13px}
code{background:#f4f4f4;padding:.1rem .3rem}
pre code{background:none;padding:0}
.meta{color:#666;font-size:13px;margin:-.5rem 0 1.5rem}
nav{margin-bottom:2rem;font-size:13px}
ul.notes{list-style:none;padding:0}
ul.notes li{margin:.3rem 0}
footer{margin-top:3rem;color:#666;font-size:12px;border-top:1px solid #eee;padding-top:1rem}
"""


def page(body, title=None):
    t = title or SITE_TITLE
    return (
        "<!doctype html>\n<html lang=en>\n<head>\n"
        '<meta charset=utf-8>\n'
        '<meta name="viewport" content="width=device-width,initial-scale=1">\n'
        f"<title>{escape(t)}</title>\n"
        f"<style>{PAGE_CSS}</style>\n"
        "</head>\n<body>\n"
        f"{body}\n"
        '<footer>Agent-readable: <a href="/llms.txt">llms.txt</a> · '
        '<a href="/notes/index.json">manifest</a> · '
        '<a href="/feed.xml">atom</a></footer>\n'
        "</body>\n</html>\n"
    )


def load_notes():
    notes = []
    for p in sorted(SRC.glob("*.md")):
        text = p.read_text(encoding="utf-8")
        meta, body = parse_frontmatter(text)
        meta.setdefault("title", p.stem)
        meta.setdefault("date", "1970-01-01")
        meta.setdefault("tags", [])
        meta.setdefault("status", "public")
        meta["slug"] = p.stem
        meta["body"] = body
        notes.append(meta)
    # newest first
    notes.sort(key=lambda n: str(n.get("date", "")), reverse=True)
    return notes


def atom_date(d):
    try:
        dt = datetime.datetime.strptime(str(d), "%Y-%m-%d")
        return dt.strftime("%Y-%m-%dT00:00:00Z")
    except Exception:
        return "1970-01-01T00:00:00Z"


def build():
    if OUT.exists():
        # wipe only contents
        for child in OUT.glob("**/*"):
            if child.is_file():
                child.unlink()
    else:
        OUT.mkdir()
    (OUT / ".well-known").mkdir(exist_ok=True)
    (OUT / "notes").mkdir(exist_ok=True)

    notes = [n for n in load_notes() if n.get("status") == "public"]

    # --- per-note .md and .html ---
    for n in notes:
        slug = n["slug"]
        md_path = OUT / "notes" / f"{slug}.md"
        md_path.write_text(n["body"], encoding="utf-8")

        body_html = md_to_html(n["body"])
        tags = ", ".join(n["tags"]) if isinstance(n["tags"], list) else n["tags"]
        note_body = (
            f"<h1>{escape(str(n['title']))}</h1>\n"
            f'<div class=meta>{escape(str(n["date"]))}'
            + (f" · {escape(tags)}" if tags else "")
            + f' · <a href="/notes/{slug}.md">.md</a></div>\n'
            + body_html
        )
        html_path = OUT / "notes" / f"{slug}.html"
        html_path.write_text(page(note_body, title=str(n["title"])), encoding="utf-8")

    # --- index.html ---
    items = "\n".join(
        f'<li><time>{escape(str(n["date"]))}</time> '
        f'<a href="/notes/{n["slug"]}.html">{escape(str(n["title"]))}</a> '
        f'<a href="/notes/{n["slug"]}.md" class=raw>[md]</a></li>'
        for n in notes
    )
    idx_body = (
        f"<h1>{escape(SITE_TITLE)}</h1>\n"
        f"<p>{escape(DESCRIPTION)}</p>\n"
        f'<ul class=notes>\n{items}\n</ul>\n'
    )
    (OUT / "index.html").write_text(page(idx_body), encoding="utf-8")

    # --- notes/index.json manifest ---
    manifest = [
        {
            "id": n["slug"],
            "title": n["title"],
            "date": n["date"],
            "tags": n["tags"] if isinstance(n["tags"], list) else [n["tags"]],
            "url_html": f"{SITE_URL}/notes/{n['slug']}.html",
            "url_md": f"{SITE_URL}/notes/{n['slug']}.md",
        }
        for n in notes
    ]
    (OUT / "notes" / "index.json").write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )

    # --- llms.txt (llmstxt.org v2) ---
    llms = f"# {SITE_TITLE}\n\n> {DESCRIPTION}\n\n"
    llms += (
        "This site publishes minor research notes. Every note has a Markdown "
        "version at the same URL with .md appended; agents should prefer those. "
        "A concatenated dump of all notes is at /llms-full.txt for grep-based "
        "retrieval. A machine-readable manifest is at /notes/index.json.\n\n"
    )
    llms += "## Notes\n"
    for n in notes:
        llms += f"- [{n['title']}]({SITE_URL}/notes/{n['slug']}.md): {n['date']}"
        tags = n["tags"] if isinstance(n["tags"], list) else [n["tags"]]
        if tags:
            llms += f" [{', '.join(tags)}]"
        llms += "\n"
    llms += "\n## Optional\n"
    llms += f"- [Manifest]({SITE_URL}/notes/index.json)\n"
    llms += f"- [Full text dump]({SITE_URL}/llms-full.txt)\n"
    llms += f"- [Atom feed]({SITE_URL}/feed.xml)\n"
    (OUT / "llms.txt").write_text(llms, encoding="utf-8")

    # --- llms-full.txt ---
    full = []
    for n in notes:
        full.append(f"# {n['title']}\n# date: {n['date']}\n# url: {SITE_URL}/notes/{n['slug']}.md\n")
        full.append(n["body"].rstrip() + "\n\n---\n")
    (OUT / "llms-full.txt").write_text("\n".join(full), encoding="utf-8")

    # --- feed.xml (Atom) ---
    updated = atom_date(notes[0]["date"]) if notes else "1970-01-01T00:00:00Z"
    feed = [
        '<?xml version="1.0" encoding="utf-8"?>',
        '<feed xmlns="http://www.w3.org/2005/Atom">',
        f"<title>{escape(SITE_TITLE)}</title>",
        f'<link href="{SITE_URL}/feed.xml" rel="self"/>',
        f'<link href="{SITE_URL}/"/>',
        f"<id>{SITE_URL}/</id>",
        f"<updated>{updated}</updated>",
        f"<author><name>{escape(SITE_AUTHOR)}</name></author>",
    ]
    for n in notes:
        feed.append("<entry>")
        feed.append(f"<title>{escape(str(n['title']))}</title>")
        feed.append(f'<link href="{SITE_URL}/notes/{n["slug"]}.md"/>')
        feed.append(f"<id>{SITE_URL}/notes/{n['slug']}.md</id>")
        feed.append(f"<updated>{atom_date(n['date'])}</updated>")
        feed.append(f"<published>{atom_date(n['date'])}</published>")
        body_escaped = escape(n["body"])
        feed.append(f'<content type="text/markdown">{body_escaped}</content>')
        feed.append("</entry>")
    feed.append("</feed>")
    (OUT / "feed.xml").write_text("\n".join(feed) + "\n", encoding="utf-8")

    # --- sitemap.xml ---
    urls = [f"{SITE_URL}/"]
    for n in notes:
        urls.append(f"{SITE_URL}/notes/{n['slug']}.html")
        urls.append(f"{SITE_URL}/notes/{n['slug']}.md")
    sm = ['<?xml version="1.0" encoding="utf-8"?>',
          '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for u in urls:
        sm.append(f"<url><loc>{escape(u)}</loc></url>")
    sm.append("</urlset>")
    (OUT / "sitemap.xml").write_text("\n".join(sm) + "\n", encoding="utf-8")

    # --- robots.txt ---
    (OUT / "robots.txt").write_text(
        "User-agent: *\nAllow: /\n\n"
        f"Sitemap: {SITE_URL}/sitemap.xml\n",
        encoding="utf-8",
    )

    # --- .well-known/agent.json ---
    agent = {
        "name": SITE_AUTHOR,
        "site": SITE_URL,
        "description": DESCRIPTION,
        "notes_manifest": f"{SITE_URL}/notes/index.json",
        "llms_txt": f"{SITE_URL}/llms.txt",
        "llms_full": f"{SITE_URL}/llms-full.txt",
        "feed": f"{SITE_URL}/feed.xml",
        "preferred_format": "text/markdown",
        "note_url_pattern": f"{SITE_URL}/notes/<id>.md",
    }
    (OUT / ".well-known" / "agent.json").write_text(
        json.dumps(agent, indent=2) + "\n", encoding="utf-8"
    )

    # --- .nojekyll so GitHub Pages serves dotfiles & .md as-is ---
    (OUT / ".nojekyll").write_text("", encoding="utf-8")

    print(f"Built {len(notes)} note(s) into docs/")
    for n in notes:
        print(f"  {n['date']}  {n['slug']}.md  — {n['title']}")


if __name__ == "__main__":
    build()
