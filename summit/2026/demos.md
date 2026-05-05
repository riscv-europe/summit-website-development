---
title: Demos
layout: summit2026
---

{% assign demos = site.data.summit2026.demos %}

{% include bannerimg.html
    img = "media/banners/banner.jpg"
%}

{% include jumboboxstart.html 
    title = "Demos"
    lead = "Notes for academic demo presenters"
%}

TBD.

<!-- Preparation before the conference: -->
<!--  - Demos shall be printed in **A0 format in portrait mode**. -->
<!--  - Each presenter shall **bring their own demo on site**. -->
<!--  - There is no template for demos. -->
<!--  - Make sure that the demo is easy to read from distance and -->
<!--    attracts people, **use QR codes to link to more content**. -->
<!--  - **At least one author of the demo must register for the core -->
<!--    conference** (Tuesday 9 to Thursday 11). -->
<!--  - Upload **ASAP an update your PDF abstract** on the submission web -->
<!--    site: -->
<!--    * To **add the authors' names** if the submission was *blind*. -->
<!--    * To fix typos, if any, if your submission was *non-blind*. -->
<!--  - **Upload your demo PDF** on the submission web site before Friday -->
<!--    May 19th [AOE (Anywhere on -->
<!--    Earth)](https://en.wikipedia.org/wiki/Anywhere_on_Earth). -->

<!-- If you want to **print your demo on-site** instead of bringing it -->
<!-- from home to Bologna, here is a list of print shops in downtdown -->
<!-- Bologna. Do not hesitate to contact them directly: -->

<!--  - [Copisteria Belle Arti](https://copisteriabellearti.blogspot.com). -->
<!--  - [Centro Stampa Zamboni](https://www.centrostampazamboni.com). -->
<!--  - [University Copy](https://universitycopy.it). -->
<!--  - [Copisteria Asterisco](https://www.asterisco.srl). -->
<!--  - [Emergenza Tesi](https://www.emergenzatesi.it). -->

<!-- At the conference: -->
<!--  - Each demos will be **displayed for a full day**. -->
<!--  - You will **mount your own demo**, no own tape allowed, you will -->
<!--    get some. -->
<!--  - Presenters are **expected to stand next to their demos** during -->
<!--    breaks and lunches. -->
<!--  - The exhibition and demo area will be **open only during breaks -->
<!--    and lunches**. -->
<!--  - The absracts and demo PDFs will be **published online** on the -->
<!--    conference web site. -->

{% include jumboboxend.html %}

{% include jumboboxstart.html 
    title = "Accepted demos"
    lead = "<strong>Check this page regularly for the schedule and location of demos!</strong>"
%}

<p style="width:50%;text-align:center;margin-left:25%"> Demos will
<strong>soon be dispatched over the three days</strong> of the core
conference<br>(Tuesday 9 to Thursday 11).<br></p>

{% for demo in demos %}

<hr style="width:50%;;margin-left:25%">
<h3 id="P">{{ demo['Title'] }}</h3>

<p style="font-size: 80%;">
Sub. #{{ demo['Id'] }}.
</p>

{% if demo['Authors'] %}{{ demo['Authors'] }}.{% endif %}

{% if demo['Abstract'] %}**Abstract**: {{ demo['Abstract'] }} {% endif %}

{% endfor %}

{% include jumboboxend.html %}

