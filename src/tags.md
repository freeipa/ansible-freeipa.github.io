---
layout: home
title: Tags
---

# {{ page.title }}

<!-- sort tags by name -->
{% capture site_tags %} 
{% for tag in site.tags %}
    {{ tag | first }}{% unless forloop.last %},{% endunless %}
{% endfor %}
{% endcapture %}
{% assign tags_list = site_tags | split:',' | sort_natural %}

<!-- List all tags with links to docs -->
{% for tag in tags_list %}
{% assign tag_name = tag | strip %}
# {{ tag_name }}
{% assign posts = site.tags[tag_name] %}
{% for post in posts %}* [{{ post.title }}]({{ post.url }})
{% endfor %}

{% endfor %}

