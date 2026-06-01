---
title: Presentations
layout: summit2026
---

{% assign presentations = site.data.summit2026.integrated.presentations %}

{% include bannerimg.html
    img = "media/banners/banner.jpg"
%}

{% include jumboboxstart.html 
    title = "Presentations"
    lead = "Notes for speakers"
%}

Preparation before the conference:
 - **At least one author of the presentation must register for the
   core conference** (Tuesday 9 to Thursday 11).
 - There are no templates for slides.
 - Upload **ASAP an update your PDF abstract** on the submission web
   site:
   * To **add the authors' names** if the submission was *blind*.
   * To fix typos, if any, if your submission was *non-blind*.
 - Before Friday May 29th, [AOE (Anywhere on
  Earth)](https://en.wikipedia.org/wiki/Anywhere_on_Earth):
   * **Upload your slides as PDF or PPTX** on the submission web site.
   * **Upload your poster as PDF** on the submission web site.

At the conference:
 - **Get in touch with your session chair** during the previous half-day,
   or early on Tuesday for talks of Tuesday 9 morning.
 - Your absract, slide and poster (if any) will be **published
   online** as PDFs on the conference web site:
   * The **abstract** will be published **as soon as** we get it.
   * The **poster, if any,** slightly before, of **at the Summit's opening**.
   * The **slides** will be pushed online **after** the Summit.

{% include jumboboxend.html %}

{% include jumboboxstart.html 
    title = "Accepted presentations"
    lead = "<strong>Check this page regularly for the final schedule!</strong>"
%}

<p style="width:50%;text-align:center;margin-left:25%"> Accepted
<strong>presentations will be associated with keynotes and invited
talks</strong> into consistent pleanary sessions, over the three days
of the core conference.<br>(Tuesday 9 to Thursday 11).<br></p>

Distributed over three days:
 - <a href="#Tue">Presentations of Tuesday 9th</a>
 - <a href="#Wed">Presentations of Wednesday 1Oth</a>
 - <a href="#Thu">Presentations of Thursday 11th</a>

{% include jumboboxend.html %}

{% include jumboboxstart.html
    title = "Tuesday 9 presentations"
    lead =  "Sorted by start time."
	id =    "Tue"
%}

{% assign day = "09-Tue" %}
{% assign dayLong = "Tuesday 9" %}
{% include summit26presentations-of-day.md day=day dayLong=dayLong presentations=presentations %}

{% include jumboboxend.html %}


{% include jumboboxstart.html
    title = "Wednesday 10 presentations"
    lead =  "Sorted by start time."
	id =    "Wed"
%}

{% assign day = "10-Wed" %}
{% assign dayLong = "Wednesday 10" %}
{% include summit26presentations-of-day.md day=day dayLong=dayLong presentations=presentations %}

{% include jumboboxend.html %}


{% include jumboboxstart.html
    title = "Thursday 11 presentations"
    lead =  "Sorted by start time."
	id =    "Thu"
%}

{% assign day = "11-Thu" %}
{% assign dayLong = "Thusrday 11" %}
{% include summit26presentations-of-day.md day=day dayLong=dayLong presentations=presentations %}

{% include jumboboxend.html %}
