---
title: Posters
layout: summit2025
---

{% include jumboboxstart.html 
    title = "Posters"
    lead = "**Notes for poster presenters**"
%}

Preparation before the conference:
 - Posters shall be printed in **A0 format in portrait mode**.
 - Each presenter shall bring their own poster on site.
 - There is no template for posters.
 - Make sure that the poster is easy to read from distance and
   attracts people, use QR codes to link to more content.
 - At least one author of the poster must register for the core
   conference (Tuesday 13 to Thursday 15).

At the conference:
 - You will mount your own poster, no own tape allowed, you will get
   some.
 - Each poster will be displayed for a full day.
 - Presenters are expected to stand next to their posters during
   breaks and lunches.
 - The exhibition and poster area will be open only during breaks and
   lunches.

{% include jumboboxend.html %}

{% assign posters_pure           = site.data.summit25posters | where: 'Acceptance Status', 'Accept as poster' %}
{% assign presentation_technical = site.data.summit25posters | where: 'Acceptance Status', 'Accept as presentation' %}
{% assign presentation_industry  = site.data.summit25posters | where: 'Acceptance Status', 'Accept as presentation (industry)' %}

{% assign posters = posters_pure | concat: presentation_technical | concat: presentation_industry %}

{% include jumboboxstart.html
    title = "Posters of Tuesday 13"
    lead =  "Sorted by expo level, poster island, and stand."
%}

{% assign day = "Tue" %}
{% assign dayLong = "Tuesday 13" %}
{% include summit25posters-of-day.md day=day dayLong=dayLong posters=posters %}

{% include jumboboxend.html %}

{% include jumboboxstart.html
    title = "Posters of Wednesday 14"
    lead =  "Sorted by expo level, poster island, and stand."
%}

{% assign day = "Wed" %}
{% assign dayLong = "Wednesday 14" %}
{% include summit25posters-of-day.md day=day dayLong=dayLong posters=posters %}

{% include jumboboxend.html %}

{% include jumboboxstart.html 
    title = "Posters of Thursday 15"
    lead =  "Sorted by expo level, poster island, and stand."
%}

{% assign day = "Thu" %}
{% assign dayLong = "Thursday 15" %}
{% include summit25posters-of-day.md day=day dayLong=dayLong posters=posters %}

{% include jumboboxend.html %}
