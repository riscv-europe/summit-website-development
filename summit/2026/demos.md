---
title: Demos
layout: summit2026
---

{% assign demos = site.data.summit2026.integrated.demos | sort: 'Island' %}

{% include bannerimg.html
    img = "media/banners/banner.jpg"
%}

{% include jumboboxstart.html
    title = "3 days of demos"
    lead =  "RISC-V in action!"
	id =    "summary"
%}


Distributed over three days:
 - <a href="#Tue">Demos of Tuesday 9th</a>
 - <a href="#Wed">Demos of Wednesday 1Oth</a>
 - <a href="#Thu">Demos of Thursday 11th</a>

{% include jumboboxend.html %}

{% include jumboboxstart.html
    title = "Tuesday 9 demos"
    lead =  "Sorted by start time."
	id =    "Tue"
%}

{% assign day = "09-Tue" %}
{% assign dayLong = "Tuesday 9" %}
{% include summit26demos-of-day.md day=day dayLong=dayLong demos=demos %}

{% include jumboboxend.html %}


{% include jumboboxstart.html
    title = "Wednesday 10 demos"
    lead =  "Sorted by start time."
	id =    "Wed"
%}

{% assign day = "10-Wed" %}
{% assign dayLong = "Wednesday 10" %}
{% include summit26demos-of-day.md day=day dayLong=dayLong demos=demos %}

{% include jumboboxend.html %}


{% include jumboboxstart.html
    title = "Thursday 11 demos"
    lead =  "Sorted by start time."
	id =    "Thu"
%}

{% assign day = "11-Thu" %}
{% assign dayLong = "Thusrday 11" %}
{% include summit26demos-of-day.md day=day dayLong=dayLong demos=demos %}

{% include jumboboxend.html %}
