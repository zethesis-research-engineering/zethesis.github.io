---
layout: page
title: Technical Notes
permalink: /technical-notes/
---

Short, practical notes on simulation, numerical methods, CFD workflows and scientific software — written from real engineering problems rather than textbook cases. Grouped by topic; newest first within each.

{% if site.posts.size > 0 %}
{% for topic in site.note_topics %}
{% assign topic_posts = site.posts | where: "topic", topic %}
{% if topic_posts.size > 0 %}
## {{ topic }}

{% for post in topic_posts %}
- [{{ post.title }}]({{ post.url | relative_url }}) — {{ post.date | date: "%Y-%m-%d" }}
{% endfor %}
{% endif %}
{% endfor %}
{% assign untagged = site.posts | where_exp: "p", "p.topic == nil" %}
{% if untagged.size > 0 %}
## Other

{% for post in untagged %}
- [{{ post.title }}]({{ post.url | relative_url }}) — {{ post.date | date: "%Y-%m-%d" }}
{% endfor %}
{% endif %}
{% else %}
_First notes are in preparation — check back soon._
{% endif %}
