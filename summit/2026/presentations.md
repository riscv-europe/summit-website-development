---
title: Presentations
layout: summit2026
---

{% assign posters = site.data.summit2026.talks %}

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

