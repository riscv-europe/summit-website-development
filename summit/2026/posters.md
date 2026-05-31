---
title: Posters
layout: summit2026
---

{% assign posters = site.data.summit2026.integrated.posters | sort: 'Island' %}

{% include bannerimg.html
    img = "media/banners/banner.jpg"
%}

{% include jumboboxstart.html
    title = "3 days of posters"
    lead =  "More than 200 posters..."
	id =    "summary"
%}

...distributed over three days and four posters islands:
 - <a href="#Tue">Posters of Tuesday 9th</a>
 - <a href="#Wed">Posters of Wednesday 1Oth</a>
 - <a href="#Thu">Posters of Thursday 11th</a>

The notes for posters presenters are [down below](#notes-to-presenters).

{% include jumboboxend.html %}

{% include jumboboxstart.html
    title = "Tuesday 9 posters"
    lead =  "Sorted by poster island."
	id =    "Tue"
%}

{% assign day = "09-Tue" %}
{% assign dayLong = "Tuesday 9" %}
{% include summit26posters-of-day.md day=day dayLong=dayLong posters=posters %}

{% include jumboboxend.html %}


{% include jumboboxstart.html
    title = "Wednesday 10 posters"
    lead =  "Sorted by poster island."
	id =    "Wed"
%}

{% assign day = "10-Wed" %}
{% assign dayLong = "Wednesday 10" %}
{% include summit26posters-of-day.md day=day dayLong=dayLong posters=posters %}

{% include jumboboxend.html %}


{% include jumboboxstart.html
    title = "Thursday 11 posters"
    lead =  "Sorted by poster island."
	id =    "Thu"
%}

{% assign day = "11-Thu" %}
{% assign dayLong = "Tusrday 11" %}
{% include summit26posters-of-day.md day=day dayLong=dayLong posters=posters %}

{% include jumboboxend.html %}

{% include jumboboxstart.html 
    title = "Posters"
    lead = "Notes for poster presenters"
	id="notes-to-presenters"
%}

Preparation before the conference:
 - Posters shall be printed in **A0 format in portrait mode**.
 - Each presenter shall **bring their own poster on site**.
 - There is no template for posters.
 - Make sure that the poster is easy to read from distance and
   attracts people, **use QR codes to link to more content**.
 - **At least one author of the poster must register for the core
   conference** (Tuesday 9 to Thursday 11).
 - Upload **ASAP an update your PDF abstract** on the submission web
   site:
   * To **add the authors' names** if the submission was *blind*.
   * To fix typos, if any, if your submission was *non-blind*.
 - **Upload your poster PDF** on the submission web site before Friday
   May 29th [AOE (Anywhere on
   Earth)](https://en.wikipedia.org/wiki/Anywhere_on_Earth).

If you want to **print your poster on-site** instead of bringing it
from home to Bologna, here is a list of print shops in downtdown
Bologna. Do not hesitate to contact them directly:

 - [Copisteria Belle Arti](https://copisteriabellearti.blogspot.com).
 - [Centro Stampa Zamboni](https://www.centrostampazamboni.com).
 - [University Copy](https://universitycopy.it).
 - [Copisteria Asterisco](https://www.asterisco.srl).
 - [Emergenza Tesi](https://www.emergenzatesi.it).

At the conference:
 - Each posters will be **displayed for a full day**.
 - You will **mount your own poster**, no own tape allowed, you will
   get some.
 - Presenters are **expected to stand next to their posters** during
   breaks and lunches.
 - The exhibition and poster area will be **open only during breaks
   and lunches**.
 - The absracts and poster PDFs will be **published online** on the
   conference web site.

{% include jumboboxend.html %}
