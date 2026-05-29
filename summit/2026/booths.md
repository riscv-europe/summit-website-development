---
title: Booths
layout: summit2026
---

{% assign sponsorsAlpha = site.data.summit2026.sponsors | sort: 'SponsorId' %}
{% assign sponsorsBooth = site.data.summit2026.sponsors | sort: 'BoothId' %}

<a id="map"></a>

{% include bannerimg.html
    img = "media/banners/booth-allocation.png"
%}

{% include jumboboxstart.html
    title = "Navigate the exhibition"
    lead = "Find the booths of the Summit's sponsors"
%}

<h2>Booths</h2>
<p>Find the sponsor from the booth number:</p>
{% for sponsor in sponsorsBooth -%}
{%- if sponsor['SponsorId'] -%}<a href="#booth-{{ sponsor['BoothId'] }}">{{ sponsor['BoothId'] }}</a>&nbsp;{%- endif -%}
{%- endfor %}

<h2>Sponsors, in alphabetical order</h2>
<p>The listing of all sponsors, their industries, booth and offering.</p>
{% for sponsor in sponsorsAlpha %}
{% if sponsor['SponsorId'] %}
<h3 id="booth-{{ sponsor['BoothId'] }}">&mdash; {{ sponsor['FullName'] }}</h3>
<p> Booth: {{ sponsor['BoothId'] }} &mdash; {{ sponsor['SponsoringLevel'] }}
{% if sponsor['Industries'] -%}&mdash; <emph>{{ sponsor['Industries'] }}</emph>{%- endif %}</p>
{%- if sponsor['OnTheBooth'] -%} <p>{{ sponsor['OnTheBooth'] }}</p>{%- endif -%}
<p><emph><a href="#map">Back to the map</a></emph></p>
{% endif %}
{% endfor %}

{% include jumboboxend.html %}
