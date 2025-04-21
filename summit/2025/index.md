---
title: Welcome
layout: summit2025
---

{% include bannerimg.html
    img = "media/banners/banner-official.png"
%}

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

**RISC-V Summit Europe** takes place in **Paris** from **Monday 12th to
Thursday 15th May, 2025**. The combination of strong industrial and
academic communities is key to the success of RISC-V in Europe, and
for this reason the conference is designed to help attendees to
explore both commercial and research applications.  *RISC-V Summit
Europe* is an opportunity not to be missed. Come to Paris to be part
of the new wave of European computing innovation!

{% include jumboboxend.html %}

{% include jumboboxstart.html
title = "Summit Overview"
lead = "Get up to speed on Monday and dive into three days of RISC-V news!"
%}

{% include bannerimg.html
    img = "media/banners/schedule-mon-thu.png"
%}

{% include jumboboxend.html %}

{% include jumboboxstart.html
title = "Keynotes & Invited Talks"
lead = "Learn about the exciting progress of RISC-V across industries and the hardware/software stack from our keynote speakers and invited talks."
%}

<div class="row mt-5">
{% assign talks = site.data.talks-details | where: "Status", "OkToPublish" | sort: "LastName" %}
{% for talk in talks %}
{% if talk['TalkKind'] == "InvitedKeynote" or talk['TalkKind'] == "InvitedPres" or talk['TalkKind'] == "SponsorKeynote" %}
{% include summit25talk-short.md talk=talk %}
{% endif %}
{% endfor %}
</div>

{% assign talks = site.data.talks-details | where: "Status", "OkToPublish" | sort: "Session" %}
{% assign agenda  = site.data.summit-agenda %}
{% assign config  = site.data.sessions-config %}
{% for talk in talks %}
{% if talk['TalkKind'] == "InvitedKeynote" or talk['TalkKind'] == "InvitedPres" or talk['TalkKind'] == "SponsorKeynote" %}
<hr style="width:50%;;margin-left:25%">
{% assign slot_ = agenda  | where: 'SlotId', talk['Session'] %}
{% assign slot  = slot_[0] %}
{% assign session_  = config | where: "SessionId", slot.SessionId %}
{% assign session   = session_[0] %}
{% include summit25talk-long.md talk=talk slot=slot session=session %}
{% endif %}
{% endfor %}

{% include jumboboxend.html %}
