---
layout: page
title: Technical Notes
permalink: /technical-notes/
---

Short, practical notes on simulation, numerical methods, CFD workflows and scientific software — written from real engineering problems rather than textbook cases.

## Notes

{% if site.posts.size > 0 %}
{% for post in site.posts %}
- [{{ post.title }}]({{ post.url | relative_url }}) — {{ post.date | date: "%Y-%m-%d" }}
{% endfor %}
{% else %}
_First notes are in preparation — check back soon._
{% endif %}
