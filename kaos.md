---
layout: page
title: KAOS
permalink: /kaos/
---

KAOS is our uncertainty-quantification capability for CFD. It is built on polynomial chaos, which is where the name comes from. A single simulation gives you one answer. KAOS tells you how much to trust it.

## The question we answer

*How sensitive is this CFD result to its inputs — and how much can I trust those inputs in the first place?*

Most RANS CFD is run deterministically: fixed boundary conditions, fixed model coefficients, one result. A more rigorous study might try a few turbulence models or meshes. But the inputs themselves are never exact — Reynolds number, inlet turbulence, incidence and the closure coefficients of a turbulence or transition model all carry uncertainty. That matters most exactly where the physics is delicate: low-Reynolds and transition-sensitive flows, where a small change in operating point moves a separation bubble and swings the predicted loss. A single number, with no confidence bound, is a fragile basis for a design decision or for reconciling a simulation with experiment.

## What KAOS does

- **Uncertainty propagation** — non-intrusive polynomial chaos expansion (PCE) turns uncertain inputs into full output distributions and confidence intervals.
- **Global sensitivity** — Sobol indices come directly out of the PCE, at no extra cost, ranking which inputs actually drive the scatter.
- **Bayesian calibration** — inferring model coefficients from data, with their uncertainty, instead of hand-tuning to a single case.
- **Surrogate models** — a validated expansion that evaluates in milliseconds, for fast what-if studies and robust design.

## CFD-native, and deliberately focused

KAOS wraps your solver as a black box, so it needs no changes to the flow solver itself. It is built around the quantities turbomachinery and aerodynamics engineers care about: loss coefficient, deviation, separation extent. And it is deliberately narrow. It does uncertainty quantification well, on a small number of solver runs, rather than trying to be a general-purpose analysis suite. That focus is what keeps it cheap to run and honest about what it claims.

KAOS is a capability we are building and delivering through consulting, or as a stand-alone application. If uncertainty, sensitivity or model calibration matters for your problem, the best starting point is a conversation.

<p><a class="btn btn-primary" href="/consulting/">Book a free call</a></p>
