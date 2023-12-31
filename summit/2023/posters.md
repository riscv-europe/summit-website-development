---
title: Posters
layout: summit2023
---

{% include jumboboxstart.html 
    title = "Posters"
%}

This page lists posters accepted for publication.

Quick link to reach posters presented each day:

 - [Tuesday 6th](#posters-on-display-tuesday-june-6th).
 - [Wednesday 7th](#posters-on-display-wednesday-june-7th)
 - [Thursday 8th](#posters-on-display-thursday-june-8th).

Posters are sorted by alphabetical order of presenter's last name.

But first of all, a few remarks for the poster presenters:

 - Preparation before the conference:
   - Posters shall be printed in A0 format, in portrait mode.
   - Each presenter shall bring his own poster on site.
   - There are no *RISC-V Summit Europe* template for posters.
   - The final version of the two pages extended abstract shall be
     povided according to the template provided in
     <https://github.com/riscv-europe/riscv-europe-summit-templates>.
 - About poster sessions:
   - As far as possible, posters have been dispatched throughout the
     three days to match topics addressed in the plenary track of the
     day.
   - Each poster will be displayed for a full day.
   - Presenters are expected to stand next to their posters during
     breaks, lunches, and during the early evening cocktail on Tuesday
     6th.
   - In order to allow authors to attend the conference pleanry track,
     the exhibition and poster area will be open only during breaks
     and lunches, plus on Tuesday 6th, during the on-site cocktail in
     late afternoon.
 - Administrativia:
   - At least one author of the poster must register for the core
     conference (Tue-Thu). Posters without registered authors will not
     be put on display nor referenced on the web site.
 - Publication on the conference web site:
   - The final version of the extended abstract shall be provided as
     PDF before the conference for publication on the web site.
   - A < 150 words summary, a < 150 words bio of the presenter,
     together with his affiliation and URLs shall be provided by mail
     to be used in the program on the conference web site.
   - The final version of the posters *may* also be provided for
     publication. This is not mandatory but highly recommended.
   - The final PDF version of the abstract, the 150 words bio and
     summary, and the poster PDF, if applicable, shall be sent to
     <europe-slides-posters-final@riscv.org>.

{% include jumboboxend.html %}

{% include jumboboxstart.html 
    title = "Posters on Display Tuesday June 6th"
%}

Presenters are expected to be with their poster during the morning break, lunch and afternoon break, as well as during the early evening cocktail on Tuesday 6.

{% assign posters_tue = site.data.summit23posters | where: "Day (Poster)", "Tue" | sort: "Poster board" %}
{% for poster in posters_tue %}
{% include summit23poster.md poster=poster %}
{% endfor %}

{% include jumboboxend.html %}

{% include jumboboxstart.html 
    title = "Posters on Display Wednesday June 7th"
%}

Presenters are expected to be with their poster during the morning break, lunch and afternoon break.

{% assign posters_wed = site.data.summit23posters | where: "Day (Poster)", "Wed" | sort: "Poster board" %}
{% for poster in posters_wed %}
{% include summit23poster.md poster=poster %}
{% endfor %}

{% include jumboboxend.html %}

{% include jumboboxstart.html 
    title = "Posters on Display Thursday June 8th"
%}

Presenters are expected to be with their poster during the morning break, lunch and afternoon break.

{% assign posters_thu = site.data.summit23posters | where: "Day (Poster)", "Thu" | sort: "Poster board" %}
{% for poster in posters_thu %}
{% include summit23poster.md poster=poster %}
{% endfor %}

{% include jumboboxend.html %}
