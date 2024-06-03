---
title: Posters
layout: summit2024
---

{% include jumboboxstart.html 
    title = "Posters"
    lead = "The great plenary presentations are completed by outstanding posters, which are presented at the expo floor."
%}

Quick link to reach posters presented each day:

**Notes for poster presenters**

 - Preparation before the conference:
   - Posters shall be printed in A0 format in portrait mode.
   - Each presenter shall bring their own poster on site.
   - There is no template for posters
   - Make sure that the poster is easy to read from distance and attracts people, use QR codes to link to more content
   - At least one author of the poster must register for the core conference (Tue-Thu)
 - At the conference:
   - You will mount your own poster, no own tape allowed, you will get some
   - Each poster will be displayed for a full day.
   - Presenters are expected to stand next to their posters during breaks
   - The exhibition and poster area will be open only during breaks

{% include jumboboxend.html %}

{% include jumboboxstart.html 
    title = "Posters on Tuesday, June 25th"
%}

{% assign posters_tue = site.data.summit24posters | where: "Day", "Tuesday 25th" | sort: "Stand" %}
{% for poster in posters_tue %}
{% include summit24poster.md poster=poster %}
{% endfor %}

{% include jumboboxend.html %}

{% include jumboboxstart.html 
    title = "Posters on Wednesday, June 26th"
%}

{% assign posters_tue = site.data.summit24posters | where: "Day", "Wednesday 26th" | sort: "Stand" %}
{% for poster in posters_tue %}
{% include summit24poster.md poster=poster %}
{% endfor %}

{% include jumboboxend.html %}

{% include jumboboxstart.html 
    title = "Posters on Thursday, June 27th"
%}

{% assign posters_tue = site.data.summit24posters | where: "Day", "Thursday 27th" | sort: "Stand" %}
{% for poster in posters_tue %}
{% include summit24poster.md poster=poster %}
{% endfor %}

{% include jumboboxend.html %}

