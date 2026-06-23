---
layout: page
title: Technical Notes
permalink: /technical-notes/
---

# Technical Notes

Short notes on simulation, numerical methods, CFD workflows and scientific software.

## Selected directions

- From research code to industrial software
- Validation workflows for CFD
- GPU-accelerated post-processing
- Boundary-condition diagnostics in high-order methods
- Simulation workflow automation for engineering teams

## Notes

{% for post in site.posts %}
- [{{ post.title }}]({{ post.url | relative_url }}) — {{ post.date | date: "%Y-%m-%d" }}
{% endfor %}
