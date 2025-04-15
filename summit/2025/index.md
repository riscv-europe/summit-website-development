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
{% assign speakers = site.data.invited-slots-details | where: "Status", "OkToPublish" | sort: "LastName" %}
{% for speaker in speakers %}
{% if speaker['TalkKind'] == "InvitedKeynote" or speaker['TalkKind'] == "InvitedPres" or speaker['TalkKind'] == "SponsorKeynote" %}
{% include summit25speaker-short.md speaker=speaker %}
{% endif %}
{% endfor %}
</div>

{% assign speakers = site.data.invited-slots-details | where: "Status", "OkToPublish" | sort: "Session" %}
{% assign agenda  = site.data.plenary-sessions-agenda %}
{% assign config  = site.data.plenary-sessions-config %}
{% for speaker in speakers %}
{% if speaker['TalkKind'] == "InvitedKeynote" or speaker['TalkKind'] == "InvitedPres" or speaker['TalkKind'] == "SponsorKeynote" %}
{% assign slot_ = agenda  | where: 'TalkSessionId', speaker['Session'] %}
{% assign slot  = slot_[0] %}
{% assign day_  = config | where: 'SessionId', slot['PlenarySessionId'] %}
{% assign day   = day_[0] %}
{% include summit25speaker-long.md speaker=speaker slot=slot day=day %}
{% endif %}
{% endfor %}

{% include jumboboxend.html %}

{% include jumboboxstart.html
title = "Program"
lead = "The exciting program of RISC-V Summit Europe spans <!-- a full week --> 4 days."
%}

<table class="table">
  <tr>
    <td style="width: 25%"><b>Monday, May 12</b></td>
    <td><b><i>Member and Newcomer Day</i></b><br />Tutorials for Newcomers and Experienced Professionals, and Technical Workgroup
      Meetings (members only)
	  <br/> Venue: <a href="https://maps.app.goo.gl/Q31cnRLcnvaRXa6v9"><em>La Cité des Sciences et de l'Industrie,</em> Porte de la Villette, Paris</a>.
	  <!-- <br /><a href="twgs"><b>Learn more</b></a> -->
	  </td>
  </tr>
  <tr>
    <td><b>Tuesday, May 13 to<br /> Thursday, May 15</b></td>
    <td><b><i>Main Conference Program</i></b><br />Keynotes, Plenary Presentations, Panels, Demo Theatre, Expo,
      Posters, Dev Zone
	  <br/> Venue: <a href="https://maps.app.goo.gl/Q31cnRLcnvaRXa6v9"><em>La Cité des Sciences et de l'Industrie,</em> Porte de la Villette, Paris</a>.
	  <!-- <br /><a href="conference"><b>Learn more</b></a> -->
	  </td>
  </tr>
  <tr>
    <td><b>Friday, May 16</b></td>
	<td><b><i>Side Events & Workshops</i></b><br />
	Side events, such as projects meetings and workshops, can be
	organized on Friday, May 16th.
	<br/><a href="side-events"><b>Learn more</b></a>.</td>
  </tr>
</table>

{% include jumboboxend.html %}
