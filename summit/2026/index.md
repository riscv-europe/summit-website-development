---
title: Welcome
layout: summit2026
---

{% include bannerimg.html
    img = "media/banners/banner.jpg"
%}

{% include jumboboxstart.html
	title = "Acceptance Notifications Sent!"
	lead = "The Program Committee has finalized its selection of accepted submissions."
%}

If you have not yet received the email, **you may chek for your own
paper** on the [submission web
site](https://cfp.riscv-europe.org/eu-summit-2026/login/?next=%2Feu-summit-2026%2Fcfp).

The **list of abstracts accepted** as poster or presentation will
**show up here in the comming days**.

{% include jumboboxend.html %}

{% include jumboboxstart.html
	title = "Welcome"
	lead = "The *RISC-V Summit Europe* is the premier event that connects the European movers and shakers – from industry, government, research, academia and ecosystem support – that are building the future of innovation on RISC-V."
%}

[RISC-V](https://riscv.org), the open standard [instruction set
architecture
(ISA)](https://en.wikipedia.org/wiki/Instruction_set_architecture), is
enabling a range of new applications and research that will define the
future of computing in Europe. The region has been central to RISC-V's
success, with one-third of RISC-V's global community based in Europe.

**RISC-V Summit Europe** takes place in **Bologna** from **Monday 8th
to Thursday 11th June, 2026**, with **side events** on **Friday
12th**. The combination of strong industrial and academic communities
is key to the success of RISC-V in Europe, and for this reason the
conference is designed to help attendees to explore both commercial
and research applications.  *RISC-V Summit Europe* is an opportunity
not to be missed. Come to Bologna to be part of the new wave of
European computing innovation!

{% include jumboboxend.html %}

{% include jumboboxstart.html
title = "Summit Overview"
lead = "Get up to speed on Monday, and start a full week of RISC-V news!<br><em>Schedule subject to minor adjustments. Updates to follow here.</em>"
%}

{% include bannerimg.html
    img = "media/banners/schedule-full-week.png"
%}

{% include jumboboxend.html %}

{% include jumboboxstart.html
title = "Keynotes & Invited Talks"
lead = "Learn about the exciting progress of RISC-V across industries and the hardware/software stack from our keynote speakers and invited talks<br><em>Check for upcoming updates!</em>"
%}

<div class="row mt-5">
{% assign speakers = site.data.summit2026.speakers-invited-or-sponsors | where: "Status", "OkToPublish" | sort: "LastName" %}
{% assign talks    = site.data.summit2026.talks-invited-or-sponsors    | where: "Status", "OkToPublish" %}
{% for speaker in speakers %}
  {% assign talk = talks | where: "SpeakerId", speaker.SpeakerId | first %}
  {% include summit26speaker.md speaker=speaker talk=talk %}
{% endfor %}
</div>
{% include jumboboxend.html %}

{% include jumboboxstart.html
title = "Abstracts and bios"
lead = "Highlights from RISC-V community ledears!<br><em>Check for upcoming updates!</em>"
%}
<div>
{% assign speakers = site.data.summit2026.speakers-invited-or-sponsors | where: "Status", "OkToPublish" | sort: "LastName" %}
{% assign talks    = site.data.summit2026.talks-invited-or-sponsors    | where: "Status", "OkToPublish" %}
{% assign session = "" | split: "" %}
{% assign slot    = "" | split: "" %}
{% for speaker in speakers %}
  {% assign talk = talks | where: "SpeakerId", speaker.SpeakerId | first %}
  {% if talk %}
	{% include summit26talk.md speaker=speaker talk=talk session=session slot=slot%}
  {% endif %}
{% endfor %}
</div>

{% include jumboboxend.html %}
