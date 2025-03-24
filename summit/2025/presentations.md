---
title: Presentations
layout: summit2025
---

{% include jumboboxstart.html 
    title = "Presentations"
    lead = "The list of accepted presentations."
%}

**Notes for plenary session presenters**

Before the conference:
 - Presenations shall be prepared as PPTX or PDF files.
 - The final asbtract and slides are due for Monday, April 21st, 2025.
 - At least one author of the poster must register for the core
   conference (Tuesday 13 to Thursday 15).
 - The slides will be collected beforehand and displayed from a shared
   laptop.

{% include jumboboxend.html %}

{% include jumboboxstart.html 
    title = "Industrial presentations"
    lead =  "Accepted industrial presentations, sorted by last name of main contact."
%}

{% assign presentations = site.data.summit25posters | where : "Acceptance Status", "Accept as presentation (industry)" | sort : "Main Contact Lastname" %}
{% for presentation in presentations %}
{% include summit25presentation.md presentation=presentation %}
{% endfor %}

{% include jumboboxend.html %}

{% include jumboboxstart.html 
    title = "Technical presentations"
    lead =  "Accepted technical presentations, sorted by last name of main contact."
%}

{% assign presentations = site.data.summit25posters | where : "Acceptance Status", "Accept as presentation" | sort : "Main Contact Lastname" %}
{% for presentation in presentations %}
{% include summit25presentation.md presentation=presentation %}
{% endfor %}

{% include jumboboxend.html %}
