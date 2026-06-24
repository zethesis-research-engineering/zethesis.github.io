---
layout: page
title: Consulting
permalink: /consulting/
---

Remote CFD consulting — from a first conversation to focused, paid sessions. Larger projects are scoped and quoted separately.

<!-- Cal.eu embed loader — included once for the whole page -->
<script type="text/javascript">
  (function (C, A, L) { let p = function (a, ar) { a.q.push(ar); }; let d = C.document; C.Cal = C.Cal || function () { let cal = C.Cal; let ar = arguments; if (!cal.loaded) { cal.ns = {}; cal.q = cal.q || []; d.head.appendChild(d.createElement("script")).src = A; cal.loaded = true; } if (ar[0] === L) { const api = function () { p(api, arguments); }; const namespace = ar[1]; api.q = api.q || []; if(typeof namespace === "string"){cal.ns[namespace] = cal.ns[namespace] || api;p(cal.ns[namespace], ar);p(cal, ["initNamespace", namespace]);} else p(cal, ar); return;} p(cal, ar); }; })(window, "https://cal.eu/embed/embed.js", "init");
</script>

## Free exploratory call

A 30-minute video call to understand your problem, check whether CFD is the right tool, and agree on next steps. No cost, no commitment.

<div style="width:100%;min-height:640px;overflow:auto" id="cal-exploratory"></div>
<script type="text/javascript">
  Cal("init", "exploratory", {origin:"https://cal.eu"});
  Cal.ns["exploratory"]("inline", {
    elementOrSelector:"#cal-exploratory",
    config: {"layout":"month_view"},
    calLink: "zethesis/free-exploratory-call",
  });
  Cal.ns["exploratory"]("ui", {"hideEventTypeDetails":false,"layout":"month_view"});
</script>

## CFD consulting — €150 / hour

Focused remote sessions on a concrete problem: solver setup, meshing, turbulence modelling (RANS or high-order LES), validation or post-processing. Booked and paid by the session.

<div style="width:100%;min-height:640px;overflow:auto" id="cal-consulting"></div>
<script type="text/javascript">
  Cal("init", "consulting", {origin:"https://cal.eu"});
  Cal.ns["consulting"]("inline", {
    elementOrSelector:"#cal-consulting",
    config: {"layout":"month_view"},
    calLink: "zethesis/cfd-consulting",
  });
  Cal.ns["consulting"]("ui", {"hideEventTypeDetails":false,"layout":"month_view"});
</script>

## Larger projects

Multi-day studies, full simulation campaigns and software development are scoped individually. Start with the free exploratory call, or [email us](mailto:contact@zethesis.eu) with a short description of the problem.
