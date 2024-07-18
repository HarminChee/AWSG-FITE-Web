---
title: "Research projects"
layout: gridlay
excerpt: "AWSG -- Research projects"
sitemap: false
permalink: /research.html
---

The flavor of the research in our group is one that mixes experiments with theories. We like to look for interesting and practically relevant theoretical problems to solve from our experimental results.

----------------------------
{% assign number_printed = 0 %}
{% for category in site.data.research_projects %}
  <h2 class="text-center"><b>{{ category.category }}</b></h2>
  {% for project in category.items %}
  <div class="row">
    <div class="col-md-6">
      {% if project.has_photo == 1 %}
      <img src="{{ site.url }}{{ site.baseurl }}/images/respic/{{ project.photo }}" class="img-responsive" width="100%"/>
      {% endif %}
    </div>
    <div class="col-md-6">
      <h3 class="text-center"><b>{{ project.name }}</b></h3>
      {{ project.description }}<br>
      {% if project.has_link == 1 %}
      <a href="{{ site.url }}{{ site.baseurl }}/{{ project.link }}" class="btn btn-primary">Read more</a>
      {% endif %}
    </div>
  </div>
  <hr>
  {% assign number_printed = number_printed | plus: 1 %}
  {% endfor %}
{% endfor %}
