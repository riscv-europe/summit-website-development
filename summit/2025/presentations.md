---
title: Presentations
layout: summit2025
---

{% include jumboboxstart.html 
    title = "Plenary sessions"
    lead = "Keynotes and presentations in the <b>Gaston Berger</b> amphitheatre (S2)"
%}

{% assign presentations = site.data.summit2025.asimported.summit25posters %}
{% assign invited = site.data.summit2025.asimported.talks-details %}
{% assign panels  = site.data.summit2025.asimported.panels-details %}
{% assign univdemos  = site.data.summit2025.asimported.univ-demos %}
{% assign sessions_raw = site.data.summit2025.asimported.sessions-config %}
{% assign sessions = "" | split: "" %}
{% for sess in sessions_raw %}
    {% unless sess.Kind == "None" %}
        {% assign sessions = sessions | push: sess %}
    {% endunless %}
{% endfor %}

{% include bannerimg.html
    img = "media/banners/schedule-tue-thu.png"
%}

**Notes for plenary session presenters**

Before the conference:
 - Presenations shall be prepared as PPTX or PDF files.
 - The final asbtract and slides are due for Monday, April 21st, 2025.
 - At least one author of the poster must register for the core
   conference (Tuesday 13 to Thursday 15).
 - The slides will be collected beforehand and displayed from a shared
   laptop.

At the conference:
 - Get in touch with your Session Chair long before the session.
 - Get in touch with the audio/video team 15 min. before the session.

**Quick links to sessions**

{% assign day = sessions[0].DayLong %}
- {{ day }}:&#32;
{%- for session in sessions -%}
{% if day != session.DayLong %}
{% assign day = session.DayLong %}
- {{ day }}:&#32;
{%- endif -%}
<a href="#T{{ session.SessionId }}">T{{ session.SessionId }} {{ session.Start }}–{{ session.End }}&#32;
{%- case session.Kind -%}
{%- when "Plenary" -%} plenary
{%- when "Breakfast" -%} community breakfast
{%- else -%} {% if session.Start == "13:00" %}lunch{% else %}break{% endif %} and demos
{%- endcase -%}</a>.
{% endfor %}


{% include jumboboxend.html %}

{% include jumboboxstart.html 
    title = "Plenary sessions & Demos"
    lead =  "**Keynotes**, **invited talks**, **industrial** and **technical presentations** will presented in plenary sessions in the **Gaston Berger** amphitheater. **Demos** will presented during lunches and some breaks in the **Louis Armand East** amphitheater"
%}

{% assign agenda  = site.data.summit2025.asimported.summit-agenda %}
{% for session in sessions %}
{% if session.Kind == "Plenary" %}
	{% assign kind = "Plenary keynotes and presentations in Gaston Berger amphitheater (S2)." %}
	{% assign location = "Gaston Berger (S2)" %}
{% elsif session.Kind == "Demo" %}
	{% assign kind = "Booths and posters in expo area (S1, S2, & S3).<br/>Demos in Louis Armand East amphitheater (S3)." %}
	{% assign location = "Louis Armand East (S3)" %}
{% elsif session.Kind == "None" %}
	{% assign kind = "Booths and posters in expo area (S1, S2, & S3)." %}
{% elsif session.Kind == "Breakfast" %}
	{% assign kind = "Community breakfast in Louis Armand amphitheater (S3)." %}
	{% assign location = "Louis Armand East (S3)" %}
{% endif %}
<hr>
<p id="T{{ session.SessionId }}" align="center" style="font-weight: bold; font-size: 1.875em">{{ session.DayLong }},  {{ session.Start }}-{{ session.End }}</p>
{%- if session.ChairName -%}<p align="center">Session chair: <b>{{ session.ChairName }}</b>, {{ session.ChairAffiliation }}.</p>{%- endif -%}
<p align="center" style="font-style: italic">{{ kind }}</p>
{% assign sessionId = session.SessionId %}
{% assign block = agenda | where: "SessionId", sessionId %}
{% for slot in block %}
{%- assign emptySlot = true -%}
{% assign content_s = slot.TalkId %}
{% assign content   = content_s | plus: 0 %}
{% if content != 0 %}
{% if content < 1000 %}
{%- assign emptySlot = false -%}
<hr style="width:50%;;margin-left:25%">
{% assign presentation_ = presentations | where: 'Submission ID', content_s %}
{% assign presentation  = presentation_[0] %}

### {{ presentation['Title'] | strip | strip_newlines }}

T{{ slot.SlotId }} (sub. \#{{ presentation["Submission ID"] }}), {{ session.DayShort  }} at {{ slot.Start }}, in {{ location }}.

By {% assign authors = presentation['Authors with Affiliations'] | replace: ' (BOSC)', ', BOSC' | replace: ' (', '**, ' | replace: '); ', '. **' | replace: ')', '.' -%}
**{{ authors }}

{% if presentation['Summary'] %}**Abstract**: {{ presentation['Summary'] }} {% endif %}

{% elsif content >= 1000 and content < 1600 %}
{% assign presentation_ = invited | where: 'SubmissId', content_s %}
{% assign presentation  = presentation_[0] %}
{% unless presentation.Status == "OnHold" %}
{%- assign emptySlot = false -%}
<hr style="width:50%;;margin-left:25%">
<a id="T{{ slot.SlotId }}"></a>

### {{ presentation['TalkTitle'] | strip | strip_newlines }}

T{{ slot.SlotId }}, {{ session.DayShort  }} at {{ slot.Start }}, in {{ location }}.

By **{{ presentation.FirstName | strip }} {{ presentation.LastName | strip }}**
{%- if presentation.Position -%}, {{ presentation.Position | strip }}{%- endif -%}
{%- if presentation.Company  -%}, {{ presentation.Company  | strip }}{%- endif -%}
{%- if presentation.FirstName2 -%}
,
**{{ presentation.FirstName2 | strip }} {{ presentation.LastName2 | strip }}**
{%- if presentation.Position2 -%}, {{ presentation.Position2 | strip }}{%- endif -%}
{%- if presentation.Company2  -%}, {{ presentation.Company2  | strip }}{%- endif -%}
{%- endif -%}
.

{% if presentation.TalkAbstract %}**Abstract**: {{ presentation['TalkAbstract'] | strip_newlines }} {% endif %}

{% if presentation.Bio          %}**Bio**:     *{{ presentation['Bio']  | strip | strip_newlines }}* {% endif %}

{% if presentation.Bio2         %}**Bio**:     *{{ presentation['Bio2'] | strip | strip_newlines }}* {% endif %}
{% endunless %}
{% elsif content >= 1600 and content < 2000 %}
{% assign univdemo = content_s | minus: 1500 %}
{% capture univdemo_s %}{{ univdemo }}{% endcapture %}
{% assign presentation_ = univdemos | where: 'Submission ID', univdemo_s %}
{% assign presentation  = presentation_[0] %}
{% unless presentation.Status == "OnHold" %}
{%- assign emptySlot = false -%}

### {{ presentation['Title'] | strip | strip_newlines }}

T{{ slot.SlotId }} (sub. \#{{ presentation["Submission ID"] }}), {{ session.DayShort  }} at {{ slot.Start }}, in {{ location }}.

By {% assign authors = presentation['Authors with Affiliations'] | replace: ' (BOSC)', ', BOSC' | replace: ' (', '**, ' | replace: '); ', '. **' | replace: ')', '.' -%}
**{{ authors }}

{% if presentation['Summary'] %}**Abstract**: {{ presentation['Summary'] }} {% endif %}

{% endunless %}
{% elsif content >= 2000 %}
{% assign panel_ = panels | where: 'SessionId', content_s %}
{% assign panel  = panel_[0] %}
{% unless panel.Status == "OnHold" %}

{%- assign emptySlot = false -%}
## Panel -- {{ panel.Title | strip | strip_newlines }}

T{{ slot.SlotId }}, {{ session.DayShort  }} at {{ slot.Start }}, in {{ location }}.

{% if panel.PanelistsAndAffiliation %}
Panelists: {{ panel.PanelistsAndAffiliation | strip }}.
{% endif %}

Moderator: **{{ panel.ModerName }}**
{%- if panel.ModerPosition -%}&#32;{{ panel.ModerPosition | strip }},{%- endif -%}
{%- if panel.ModerCompany  -%}&#32;{{ panel.ModerCompany  | strip }}{%- endif -%}
.

{% if panel.Argument %}**Argument**: {{ panel.Argument | strip_newlines }} {% endif %}

{% endunless %}
{% endif %}
{% endif %}
{% unless emptySlot %}<p align="center" style="font-size: 0.8em"><a href="presentations.html" class="backnavigation">To page top</a> &mdash; <a href="#T{{ session.SessionId }}" class="backnavigation">To session T{{ session.SessionId }}</a> &mdash; <a href="#T{{ slot.SlotId }}" class="backnavigation">To talk T{{ slot.SlotId }}</a></p>{% endunless %}
{% endfor %}
{% endfor %}

{% include jumboboxend.html %}
