---
title: Posters
layout: summit2025
---

{% include jumboboxstart.html 
    title = "Posters"
    lead = "**Notes for poster presenters**"
%}

{% assign posters_pure           = site.data.summit25posters | where: 'Acceptance Status', 'Accept as poster' %}
{% assign presentation_technical = site.data.summit25posters | where: 'Acceptance Status', 'Accept as presentation' %}
{% assign presentation_industry  = site.data.summit25posters | where: 'Acceptance Status', 'Accept as presentation (industry)' %}
{% assign posters = posters_pure | concat: presentation_technical | concat: presentation_industry %}

Preparation before the conference:
 - Posters shall be printed in **A0 format in portrait mode**.
 - Each presenter shall bring their own poster on site.
 - There is no template for posters.
 - Make sure that the poster is easy to read from distance and
   attracts people, use QR codes to link to more content.
 - At least one author of the poster must register for the core
   conference (Tuesday 13 to Thursday 15).

Local print shop:
 - For authors that would like to print their poster in Paris, there
   is a print shop named “[Au Print](https://auprint.fr)” located [14
   rue Rouvet, 75019
   Paris](https://maps.app.goo.gl/FZZuos9y2NQEyHv77). It is close to
   the metro station “[Corentin
   Cariou](https://www.bonjour-ratp.fr/en/stations-metro/corentin-cariou/)”,
   one stop away from the venue. The web site is in French, but they
   accept orders in English at
   [contact@auprint.fr](mailto:contact@auprint.fr) -- price is about
   40&nbsp;€ for an A0 print on 120&nbsp;g/m<sup>2</sup> paper.

At the conference:
 - You will mount your own poster, no own tape allowed, you will get
   some.
 - Each poster will be displayed for a full day.
 - Presenters are expected to stand next to their posters during
   breaks and lunches.
 - The exhibition and poster area will be open only during breaks and
   lunches.

{% include jumboboxend.html %}

{% include jumboboxstart.html
    title = "More than 180 posters over 3 days!"
    lead = "More than 60 posters per day are dispatched over a dozen of posters islands spread over the 3 levels of the expo area"
	id = "summary"
%}

To the lists of posters on display, per day:

{% assign day = "Tue" %}
{% assign dayLong = "Tuesday 13" %}
{% include summit25posters-islands.md day=day dayLong=dayLong %}

{% assign day = "Wed" %}
{% assign dayLong = "Wednesday 14" %}
{% include summit25posters-islands.md day=day dayLong=dayLong %}

{% assign day = "Thu" %}
{% assign dayLong = "Thursday 15" %}
{% include summit25posters-islands.md day=day dayLong=dayLong %}

{% include jumboboxend.html %}


{% include jumboboxstart.html
    title = "Tuesday 13 Posters"
    lead =  "Sorted by expo level, poster island, and stand."
	id =    "Tue"
%}

{% assign day = "Tue" %}
{% assign dayLong = "Tuesday 13" %}
{% include summit25posters-of-day.md day=day dayLong=dayLong posters=posters %}

{% include jumboboxend.html %}

{% include jumboboxstart.html
    title = "Wednesday 14 Posters"
    lead =  "Sorted by expo level, poster island, and stand."
	id =    "Wed"
%}

{% assign day = "Wed" %}
{% assign dayLong = "Wednesday 14" %}
{% include summit25posters-of-day.md day=day dayLong=dayLong posters=posters %}

{% include jumboboxend.html %}

{% include jumboboxstart.html
    title = "Thursday 15 Posters"
    lead =  "Sorted by expo level, poster island, and stand."
	id =    "Thu"
%}

{% assign day = "Thu" %}
{% assign dayLong = "Thursday 15" %}
{% include summit25posters-of-day.md day=day dayLong=dayLong posters=posters %}

{% include jumboboxend.html %}
