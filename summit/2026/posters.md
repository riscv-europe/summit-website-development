---
title: Posters
layout: summit2026
---

{% assign posters = site.data.summit2026.posters %}

{% include bannerimg.html
    img = "media/banners/banner.jpg"
%}

{% include jumboboxstart.html 
    title = "Posters"
    lead = "Notes for poster presenters"
%}

Preparation before the conference:
 - Posters shall be printed in **A0 format in portrait mode**.
 - Each presenter shall **bring their own poster on site**.
 - There is no template for posters.
 - Make sure that the poster is easy to read from distance and
   attracts people, **use QR codes to link to more content**.
 - **At least one author of the poster must register for the core
   conference** (Tuesday 9 to Thursday 11).
 - **Update your PDF abstract** on the submission web site:
   * To **add the authors' names** if the submission was *blind*.
   * To fix typos, if any, if your submission was *non-blind*.
 - **Upload your poster PDF** on the submission web site.

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

{% include jumboboxstart.html 
    title = "Accepted posters"
    lead = "In alphabetical order of first author"
%}

<p style="width:50%;text-align:center;margin-left:25%"> Posters will
<strong>soon be dispatched over the three days</strong> of the core
conference<br>(Tuesday 9 to Thursday 11).<br> <strong>Check this page
regularly!</strong></p>

{% for poster in posters %}

<hr style="width:50%;;margin-left:25%">
<h3 id="P">{{ poster['Title'] }}</h3>

<p style="font-size: 80%;">
Sub. #{{ poster['Id'] }}.
</p>

{% if poster['Authors'] %}{{ poster['Authors'] }}.{% endif %}

{% if poster['Abstract'] %}**Abstract**: {{ poster['Abstract'] }} {% endif %}

{% endfor %}

{% include jumboboxend.html %}

