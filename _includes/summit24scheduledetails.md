{% assign program=site.data.summit24schedule | where: "day", include.day_id %}

{% for talk in program %}
{% if talk.name %}

<a id="{{ talk.title | slugify }}-details"/>

### {{ talk.title }}

**{{ talk.name | strip }}**

*{% if talk.extra %}{{ talk.extra }}{% else %}Plenary{% endif %} on {{ include.day }} at {{ talk.time }}.*

{% if talk.video %} <a href="https://youtu.be/{{ talk.video }}"><img src="/assets/icons/youtube.svg"> Recording</a>{% endif %}{% if talk.slides %} <a href="media/proceedings/plenary/{{ talk.slides }}"><img src="/assets/icons/file-earmark-pdf.svg"> Slides</a>{% endif %}

{% if talk.abstract %}
#### Abstract

{{ talk.abstract }}
{% endif %}

{% if talk.bio %}
#### Biography

{{ talk.bio }}
{% endif %}

<div style="text-align: right" markdown="1">
<img src="/assets/icons/arrow-up.svg"/> *Back to <a href="#{{ talk.title | slugify }}">schedule</a>*
</div>
{% endif %}
{% endfor %}