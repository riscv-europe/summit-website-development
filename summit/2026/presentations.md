---
title: Presentations
layout: summit2026
---

{% assign presentations = site.data.summit2026.integrated.presentations %}

{% include bannerimg.html
    img = "media/banners/banner.jpg"
%}

{% include jumboboxstart.html 
    title = "More than 50 keynotes, talks, panels, etc."
    lead = "An event packed with news, results, demos, and networking opportunities!"
%}


The three days' program of the core conference:
 - <a href="#Tue">Presentations of Tuesday 9th</a>
 - <a href="#Wed">Presentations of Wednesday 1Oth</a>
 - <a href="#Thu">Presentations of Thursday 11th</a>

Notes for speakers are [down below](#notes).

{% include jumboboxend.html %}

{% include jumboboxstart.html
    title = "Tuesday 9"
	id =    "Tue"
%}

{% assign day = "09-Tue" %}
{% assign dayLong = "Tuesday 9" %}
{% include summit26presentations-of-day.md day=day dayLong=dayLong presentations=presentations %}

{% include jumboboxend.html %}


{% include jumboboxstart.html
    title = "Wednesday 10"
	id =    "Wed"
%}

{% assign day = "10-Wed" %}
{% assign dayLong = "Wednesday 10" %}
{% include summit26presentations-of-day.md day=day dayLong=dayLong presentations=presentations %}

{% include jumboboxend.html %}


{% include jumboboxstart.html
    title = "Thursday 11"
	id =    "Thu"
%}

{% assign day = "11-Thu" %}
{% assign dayLong = "Thusrday 11" %}
{% include summit26presentations-of-day.md day=day dayLong=dayLong presentations=presentations %}

{% include jumboboxend.html %}

{% include jumboboxstart.html 
    title = "Notes for speakers"
	id= "notes"
%}

Blind and non-blind accepted presentations have been associated with
keynotes and invited talks into consistent pleanary sessions, spaning
the three days of the core conference.

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

<p align="center" style="font-size: 0.8em">
<a class="backnavigation" href="#summary">To page top</a> &mdash;
<a href="#Tue" class="backnavigation">To presentations of Tuesday 9</a> &mdash;
<a href="#Wed" class="backnavigation">To presentations of Wednesday 10</a> &mdash;
<a href="#Thu" class="backnavigation">To presentations of Thursday 11</a>
</p>

{% include jumboboxend.html %}

<button id="jump-to-now" title="Jump to the session happening now"
        style="display:none; position:fixed; bottom:24px; right:24px; z-index:1000;
               padding:12px 18px; border:none; border-radius:24px; cursor:pointer;
               background:#f5c518; color:#000; font-weight:bold; font-size:0.95em;
               box-shadow:0 2px 10px rgba(0,0,0,0.35);">
  &#9679; Now
</button>

<script>
  (function () {
    var btn = document.getElementById('jump-to-now');
    var blocks = [].slice.call(document.querySelectorAll('.schedule-block-title[data-start]'));
    if (!blocks.length) return;

    function currentBlock() {
      var now = Date.now();
      var target = blocks[0];              // before the event -> first block
      for (var i = 0; i < blocks.length; i++) {
        // data-start carries the +02:00 offset, so this compares absolute instants;
        // the visitor's local timezone is irrelevant.
        if (Date.parse(blocks[i].dataset.start) <= now) target = blocks[i];
        else break;                        // blocks are in chronological DOM order
      }
      return target;
    }

    btn.style.display = 'inline-block';
    btn.addEventListener('click', function () {
      currentBlock().scrollIntoView({ behavior: 'smooth', block: 'start' });
    });
  })();
</script>
