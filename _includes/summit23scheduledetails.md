{% assign program=site.data.summit23schedule | where: "day", include.day_id %}

{% for talk in program %}

<a id="{{ talk.title | slugify }}"/>

### {{ talk.title }}

**{{ talk.name | strip }}**

*{% if talk.extra %}{{ talk.extra }}{% else %}Plenary{% endif %} on {{ include.day }} at {{ talk.time }}.*

{% if talk.slides %} <a href="media/proceedings/plenary/{{ talk.extended }}"><img src="/assets/icons/file-earmark-pdf.svg"> Extended Abstract</a>{% endif %} {% if talk.video %} <a href="https://youtu.be/{{ talk.video }}"><img src="/assets/icons/youtube.svg"> Recording</a>{% endif %}{% if talk.slides %} <a href="media/proceedings/plenary/{{ talk.slides }}"><img src="/assets/icons/file-earmark-pdf.svg"> Slides</a>{% endif %}

{% if talk.abstract %}
#### Abstract

{{ talk.abstract }}
{% endif %}

{% if talk.bio %}
#### Biography

{{ talk.bio }}
{% endif %}

<div style="text-align: right" markdown="1">
<img src="/assets/icons/arrow-up.svg"/> *Back to <a href="#top-tue">Tue 6th</a> - <a href="#top-wed">Wed 7th</a> - <a href="#top-thu">Thu 8th</a>.*
</div>
{% endfor %}