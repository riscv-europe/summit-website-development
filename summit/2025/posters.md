---
title: Posters
layout: summit2025
---

{% include jumboboxstart.html 
    title = "Posters"
    lead = "The list of accepted posters."
%}

**Notes for poster presenters**

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

{% include jumboboxstart.html 
    title = "Posters"
    lead =  "Sorted by last name of main contact."
%}

{% assign posters_tue = site.data.summit25posters | sort: "Main Contact Lastname" %}
{% for poster in posters_tue %}
{% if poster["Acceptance Status"] == "Accept as poster" %}
{% include summit25poster.md poster=poster %}
{% endif %}
{% endfor %}

{% include jumboboxend.html %}
