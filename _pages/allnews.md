---
title: "News"
layout: textlay
excerpt: "AWSG in CUHK"
sitemap: false
permalink: /allnews.html
---

{% for article in site.data.news %}
<div class="card">
<div class="card-body">
<h5 class="card-title">{{ article.headline }}</h5>
<h6 class="card-subtitle mb-2 text-muted">{{ article.date }}</h6>
<p class="card-text" style="font-size: 18px;">{{ article.content }}</p>
{% if article.has_link == 1%}
<a href="#" class="card-link">{{ article.link }}</a>
{% endif %}
</div>
</div>
<br>
{% endfor %}
