---
title: This site is agent-readable by default
date: 2026-11-23
tags: [meta, agents, llms-txt]
status: draft
---

This is the first note on the site, and it's also the documentation for
how the site is put together. Two goals, in priority order:

1. Be trivially readable by agents.
2. Be tolerable to look at for a human who happens to visit.

Everything else follows from those.

## What "agent-readable" means here

- Every note is written in Markdown and published as Markdown at a
  stable URL: `/notes/<id>.md`. That file is the canonical artifact.
  The `.html` version is a thin render for browsers; agents should
  fetch the `.md`.
- `/llms.txt` is an index following the [llmstxt.org](https://llmstxt.org)
  v2 convention: a short summary plus a list of links to the Markdown
  versions of every note.
- `/llms-full.txt` is every note concatenated into one grep-able file.
  If you have no fancier tool, fetch that and grep it.
- `/notes/index.json` is a machine-readable manifest with id, title,
  date, tags, and both URL forms for each note.
- `/.well-known/agent.json` points at all of the above and declares
  the preferred format.
- `/feed.xml` is an Atom feed whose entries carry the Markdown body
  in `<content type="text/markdown">`.

## What it does not do

There is no JavaScript, no tracking, no analytics, no comments, no
newsletter signup, no social embeds, no cookie banner. There is no
"About" page with a headshot and a career timeline. The index page is
a flat list of notes with dates. That's the whole site.

## How it's built

A single Python script (`build.py`, stdlib only) reads `notes/*.md`,
parses a small frontmatter block, and writes the static site into
`docs/`. No framework, no dependencies, no build pipeline beyond
`python3 build.py`. The source notes are the thing; everything in
`docs/` is derived.

The frontmatter is intentionally simple:

```
---
title: Note Title
date: 2026-11-23
tags: [ml, scaling]
status: public
---
```

`status: public` is required for a note to appear in the output.
Anything else (draft, private, etc.) is skipped — so drafts can live
in the same `notes/` directory without being published.
