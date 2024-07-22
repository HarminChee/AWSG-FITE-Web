---
title: "Research projects"
layout: gridlay
excerpt: "AWSG -- Research projects"
sitemap: false
permalink: /research.html
---

<style>
.border-box {
    border: 1px solid #ccc;
    padding: 10px;
    margin-bottom: 20px;
}
</style>

<div class="border-box">
The flavor of the research in our group is one that mixes experiments with theories. We like to look for interesting and practically relevant theoretical problems to solve from our experimental results.
</div>

{% assign number_printed = 0 %}
{% for project in site.data.research_projects %}
<div class="row">
  {% assign even_odd = number_printed | modulo: 2 %}
  <div class="col-md-6">
    <div class="border-box">
      <h3><b>{{ project.name }}</b></h3>
      {{ project.description }}<br>
      {% if project.has_link == 1 %}
      <a href="{{ site.url }}{{ site.baseurl }}/{{ project.link }}">Read more</a>
      {% endif %}
    </div>
  </div>
  <div class="col-md-6">
    {% if project.has_photo == 1 %}
    <img src="{{ site.url }}{{ site.baseurl }}/images/respic/{{ project.photo }}" class="img-responsive" width="100%"/>
    {% endif %}
  </div>
</div>
{% assign number_printed = number_printed | plus: 1 %}
{% endfor %}
