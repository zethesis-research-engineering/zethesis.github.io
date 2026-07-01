---
title: Technical Notes — editorial roadmap (internal)
---

# Technical Notes — editorial roadmap

Internal planning document. Lives in `_drafts/`, so it is NOT published
(Jekyll only builds `_drafts` when run with `--drafts`).

## Why these notes exist

Two jobs, both required:

1. **Enjoyment** — topics I actually want to work on, or I won't keep writing them.
2. **Credibility** — each note should quietly prove to a potential client that I can
   set up, run, validate and reason about real CFD problems.

The best topics sit where the two overlap.

## Format and cadence

- **Quarterly themes.** Each quarter (or 4-month block) has one lead theme.
- A theme is a **small series of 2–3 short notes**, not one giant article.
  Ship more often, keep momentum, keep the index alive.
- **Publish the code/configs on GitHub** with every hands-on note. This is the
  "research-code → reliable software" pitch in practice: builds trust, helps SEO,
  and turns the validation notes into a linkable portfolio for the Consulting page.
- Each note: short motivation → method → what to run → result/plot → takeaway → link to repo.

## Threads

| # | Thread | Appeal | Effort | Cloud cost | Client value |
|---|--------|--------|--------|-----------|--------------|
| 1 | Turbomachinery validation (SU2 / PyFR): MTU161, NASA R37/R67, supersonic cascade | high | med–high | med–high | **very high** (core domain) |
| 2 | Uncertainty quantification in SU2 (polynomial chaos, Bayesian) | high | medium | low | high (differentiator) |
| 3 | Literature review & field notes — CFD × AI/ML, HPC, GPU (Hodges-style) | high | low | none | high |
| 4 | Hypersonic flows (SU2 + Mutation++) | high | **high** | high | niche |
| 5 | Flux Reconstruction / Nodal DG in Python (from the book) | high | low | none | indirect (depth) |

Notes on the threads:

- **Thread 1** is the flagship. Start with cheap ~2D cases (MTU161, supersonic
  cascade) before spending on 3D R37/R67.
- **Thread 2** pairs with thread 1: run UQ *on top of* a validation case already computed.
  Non-intrusive PCE treats SU2 as a black box (chaospy / OpenTURNS) — little code, little compute.
- **Thread 3** is the **literature-review backbone** — see its own section below. This is
  also the authentic home for "AI" on the site: I review the CFD × ML field rather than
  claim to do all of it. **Quantum for CFD is speculative today** — cover it as "watching
  the field", not "doing".
- **Thread 4** is a year-2 stretch / single showcase piece. Big effort, smaller market.
- **Thread 5** is the best starter: zero cost, runs on a laptop, builds the foundation
  for understanding PyFR (which is FR-based).

## Year 1 calendar (quarterly)

- **Q1 — FR / DG fundamentals in Python** (thread 5)
  - **Why high-order? FR from motivation to code** — lead note, scaffolded in `_posts`
    (`published: false`). Structure: (1) why HO and not FVM, shown with a Gaussian-bump
    transport demo — high-order keeps shape/amplitude, low-order FVM diffuses, low-dissipation
    schemes disperse — as video/images; (2) short history of HO CFD (ADIGMA → IDIHOM → TILDA,
    the AIAA High-Order Workshops, HONOM); (3) FR/DG/SD as one framework via the correction
    function; (4) the 1D linear advection implementation.
  - 1D Euler (shock tube)
  - 2D scalar advection
- **Q2 — Turbomachinery validation, 2D cases** (thread 1)
  - MTU161 transonic cascade in SU2
  - Supersonic compressor cascade
- **Q3 — UQ on a validation case** (thread 2, reuses Q2)
  - Non-intrusive polynomial chaos with SU2 + chaospy
  - Bayesian calibration of a turbulence-model coefficient
- **Q4 — Turbomachinery 3D** (thread 1)
  - NASA Rotor 37 (and/or 67) RANS validation

Running underneath all of it: the **literature-review thread** below, on a steady
monthly-ish cadence. Hypersonic (thread 4) goes to the year-2 backlog.

## Literature review (the backbone)

Modelled on Justin Hodges' *Physical AI* Substack ("read what I read — code what I
code"): short, accessible reviews of what's happening at the intersection of CFD,
machine learning, HPC and GPU computing — written for practitioners, not for reviewers.

Why it's worth doing:

- **Low cost, high cadence.** No compute, no big project — it's reading plus opinion,
  so it can ship monthly and keep the site alive between the heavy quarterly series.
- **It's where AI belongs on this site.** Reviewing the field is honest and credible;
  it engages with AI/ML without overpromising services I don't offer.
- **It compounds.** A steady review habit builds an audience and quietly signals that
  I stay current — which is exactly what a consulting client wants to believe.

Format for each review (keep it tight):

- 1–3 papers or releases, grouped by a theme (e.g. ML turbulence closures, neural
  surrogates, GPU solvers, foundation models for PDEs).
- For each: **what they did**, **why it matters**, **the catch / open question**.
- A short personal **takeaway** — the opinion is the value, not the summary.
- Links to the sources; where useful, a tiny code or plot of my own
  ("code what I code") to make a point concrete.

Cadence: aim for one review per month. When a hands-on series note slips, the review
keeps the publishing rhythm going.

### Turbomachinery paper reviews (the authority angle)

Anchor the review thread on **turbomachinery**, not generic AI/ML — it's the domain I
sell, so reviewing it builds authority exactly where it converts to consulting.

- **Source:** a personal subscription to *ASME Journal of Turbomachinery* (~€250/yr).
  Use recent papers to write timely "paper of the month / recent work" reviews and build
  a name in the field.
- **Format:** pick a recent paper → what they did / why it matters / the catch → my
  takeaway as a practitioner → link to the DOI. Tie back to my own validation cases
  where relevant (e.g. "this is the kind of effect we'd see in the R37 study").
- **Copyright — important:** the subscription is for *personal* access. Do **not** re-host
  the PDFs or reproduce the paper's figures/tables on the site (that's what to *not* copy
  from Hodges). Write original summaries in my own words, quote at most a short snippet
  with attribution, and **link to the DOI** so readers get the paper from the publisher.
  Reproducing a figure requires the publisher's permission.
- **Digitising data is fine, copying the figure is not.** Copyright protects the figure's
  *expression*, not the *data* it shows. Extracting the data points (e.g. with
  WebPlotDigitizer) and making my **own** plot in Python is acceptable — it reuses facts,
  not the protected image. Always cite ("data digitized from Fig. X of [Author, year, DOI]")
  and label it as digitised/approximate. This doubles as the validation workflow: digitise
  the reference experimental data, then overlay my CFD. (Not legal advice — check edge cases.)

## Extra ideas

- **"What does it cost to run R37 on the cloud?"** — turn the compute spend into a
  benchmark note (provider / rented-GPU cost vs performance). Ties threads 1+3+5;
  nearly free because it's a by-product of the real work.
- **Meshing for turbomachinery** — a practical pain that is rarely blogged; cheap,
  high client value.
- **PyFR on a rented GPU** — performance/cost write-up; GPU-native, links the threads.

## Budget note

Only Q2 (partly) and Q4 need real cloud spend. Q1 and most of Q3 run on a laptop.
Use cheap spot / preemptible instances; start small and scale once the pipeline works.

Fixed cost: *ASME Journal of Turbomachinery* personal subscription (~€250/yr) — feeds the
turbomachinery review thread. Personal-use licence: summarise and link, never re-host PDFs.
