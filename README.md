# personal site — agent-first notes

A minimal, agent-readable personal site. Markdown notes in `notes/` are
the canonical artifact; `build.py` (Python 3 stdlib only, no
dependencies) renders a static site to `docs/`.

## Why this shape

See `notes/0001-agent-readable-by-default.md`. Short version: notes are
written for agents first, humans second. Every note is published as
Markdown at a stable URL, indexed by `llms.txt` and `notes/index.json`,
and dumped in full into `llms-full.txt`. No JavaScript, no framework,
no tracking.

## Write a note

Create `notes/<id>.md`:

```
---
title: Note Title
date: 2026-11-23
tags: [ml, scaling]
status: public
---

Markdown body...
```

`status: public` is required for the note to appear. Anything else
(draft, private) is skipped, so drafts can live alongside published
notes.

## Build

```
python3 build.py
```

Outputs to `docs/`:

```
docs/
├── index.html              flat list of notes
├── llms.txt                agent index (llmstxt.org v2)
├── llms-full.txt           all notes concatenated, grep-able
├── feed.xml                Atom feed, markdown bodies
├── sitemap.xml
├── robots.txt
├── .nojekyll
├── .well-known/agent.json
└── notes/
    ├── index.json          machine-readable manifest
    ├── <id>.md             raw markdown (canonical)
    └── <id>.html           minimal HTML render
```

## Configure

Edit the `SITE_*` constants at the top of `build.py`:

- `SITE_TITLE`, `SITE_AUTHOR`, `DESCRIPTION`
- `SITE_URL` — your github.io URL or custom domain

## Host on GitHub Pages

1. Create a public repo named `adityavram.github.io`
   (this gives you `https://adityavram.github.io`).
2. Push this directory to `main`:

   ```
   git init
   git add .
   git commit -m "initial site"
   git branch -M main
   git remote add origin git@github.com:adityavram/adityavram.github.io.git
   git push -u origin main
   ```

3. In the repo on GitHub: **Settings → Pages → Build and deployment →
   Source: Deploy from a branch → Branch: `main` / `/docs` folder**.
4. Wait a minute or two. The site appears at
   `https://adityavram.github.io`.

The `.nojekyll` file in `docs/` tells GitHub Pages to skip Jekyll and
serve files as-is, so `.md`, `.well-known/`, and `llms.txt` are all
served with correct content types.

## Custom domain (optional)

1. Buy a domain. Add an `A`/`CNAME` record pointing at GitHub Pages
   (see GitHub's docs for the current IPs / `*.github.io` CNAME).
2. Put your domain on a single line in `docs/CNAME`:
   ```
   yourdomain.com
   ```
3. Update `SITE_URL` in `build.py` to `https://yourdomain.com` and
   rebuild.
4. In the repo: **Settings → Pages → Custom domain → enter it → Enforce
   HTTPS**.
