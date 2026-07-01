---
name: zethesis-notes
description: >
  Conventions for producing figures, animations, plots, or any generated
  artifact for the Zethesis technical notes / website. Use whenever creating or
  regenerating visual/data assets for a post, or writing solver/figure tooling.
  Enforces where dev code lives, where published output goes, and forbids /tmp.
---

# Zethesis technical-notes workflow

Two sibling directories under `/home/andrea/andrea/`:

- **Site repo (published):** `zethesis.github.io` — the Jekyll site. Holds
  `_posts/`, `assets/`, pages. This is what ships to GitHub Pages.
- **Dev dir (never published):** `zethesis.github.io.dev` — all working code:
  solvers, figure/animation scripts, scratch. One folder per note,
  `note-NN-short-slug/`. Shared Python env at `zethesis.github.io.dev/.venv`.

## Hard rules

1. **Working code → the `.dev` dir, one folder per note.** Never put solver or
   figure-generation code inside the site repo.
2. **Generated output → the site repo's `assets/`**, into the right subdir:
   - images / posters → `zethesis.github.io/assets/images/`
   - videos → `zethesis.github.io/assets/video/`
   Scripts resolve these paths from their own location (the site repo is the
   sibling of `.dev`), so they write there directly — do not copy by hand.
3. **Never use `/tmp`** or any location outside these two directories — not for
   scratch, not for venvs, not for intermediate frames. Video encoders write
   their temp frames to a local `_frames_*` dir inside the note folder and
   delete them after.
4. **Verify the numerics before trusting a figure.** A figure that illustrates a
   claim must be backed by a check (convergence test, exact-solution recovery,
   conservation) — not just a plausible-looking picture.

## Running tooling

Shared venv (numpy, matplotlib already installed):
```
cd /home/andrea/andrea/zethesis.github.io.dev/<note-folder>
../.venv/bin/python <script>.py
```

## Grouping by topic

The `/technical-notes/` page groups notes by **topic** (the editorial threads),
not chronologically. Each post needs a `topic:` front-matter field whose value is
one of the entries in `note_topics` in `_config.yml` (which also sets the display
order). Within a topic, notes list newest-first. Empty topics are hidden; a post
with no `topic` falls into an "Other" bucket (so nothing is silently dropped).
Topic 1 is "Flux reconstruction"; "Test case validation" is declared and waiting.

## Embedding in a post

Reference published assets with site-absolute paths, e.g.
`/assets/video/<name>.mp4` and `/assets/images/<name>.png` (poster/fallback).

### Math (MathJax) — important kramdown gotcha
MathJax 3 renders client-side (see `_includes/head.html`), with both `$…$`/`\(…\)`
inline and `$$…$$`/`\[…\]` display. BUT kramdown does **not** protect single
`$…$`: it treats the content as ordinary text, so underscores pair into `<em>`
(`$f_{L}$ … $f_{R}$` → corrupted) and apostrophes become smart quotes. Therefore:
- In **markdown prose**, use `$$…$$` for *all* math. kramdown shields it and emits
  `\(…\)` for inline (within a paragraph) and `\[…\]` for display (own line).
- Inside **raw HTML** (e.g. a `<figcaption>`), kramdown does nothing, so write
  MathJax delimiters directly: `\(…\)` inline, `\[…\]` display. Do *not* use `$$…$$`
  there — it would render as a display block mid-caption.
- Verify after building: the article body of the built HTML should contain **no
  literal `$`** and no `<em>` inside a formula.

## Current notes
- `note-01-flux-reconstruction` → a two-part note:
  - `_posts/2026-06-25-why-high-order-flux-reconstruction.md` — "Why high-order?
    Flux reconstruction, from motivation to method" (the why/what; uses the animations).
  - `_posts/2026-06-26-smallest-high-order-solver.md` — "The smallest high-order
    solver that works" (the build; uses the convergence figure).
