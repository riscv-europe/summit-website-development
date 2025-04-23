---
title: Presentations
layout: summit2025
---

{% include jumboboxstart.html 
    title = "Plenary sessions"
    lead = "Keynotes and presentations in the <b>Gaston Berger</b> amphitheatre (level -2)"
%}

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

{% include jumboboxend.html %}

{% include jumboboxstart.html 
    title = "Plenary sessions & Demos"
    lead =  "**Keynotes**, **invited talks**, **industrial** and **technical presentations** will presented in plenary sessions in the **Gaston Berger** amphitheater. **Demos** will presented during lunches and some breaks in the **Louis Armand East** amphitheater"
%}

{% assign presentations = site.data.summit25posters %}
{% assign invited = site.data.talks-details %}
{% assign panels  = site.data.panels-details %}
{% assign sessions_raw = site.data.sessions-config %}
{% assign sessions = "" | split: "" %}
{% for sess in sessions_raw %}
    {% unless sess.Kind == "None" %}
        {% assign sessions = sessions | push: sess %}
    {% endunless %}
{% endfor %}
{% assign agenda  = site.data.summit-agenda %}
{% for session in sessions %}
{% if session.Kind == "Plenary" %}
	{% assign kind = "Plenary keynotes and presentations in Gaston Berger anphitheater (level -2)." %}
{% elsif session.Kind == "Demo" %}
	{% assign kind = "Demos in Louis Armand East amphitheater (level -3).<br/>Booths and posters in expo area's 3 levels." %}
{% elsif session.Kind == "None" %}
	{% assign kind = "Booths and posters in expo area's 3 levels." %}
{% elsif session.Kind == "Breakfast" %}
	{% assign kind = "Community breakfast in Louis Armand amphitheater (level -3)." %}
{% endif %}
<hr>
<hr>
<p align="center" style="font-weight: bold; font-size: 1.875em">{{ session.DayLong }},  {{ session.Start }}-{{ session.End }}</p>
{%- if session.ChairName -%}<p align="center">Session chair: <b>{{ session.ChairName }}</b>, {{ session.ChairAffiliation }}.</p>{%- endif -%}
<p align="center" style="font-style: italic">{{ kind }}</p>
{% assign sessionId = session.SessionId %}
{% assign block = agenda | where: "SessionId", sessionId %}
{% for slot in block %}
{% assign content_s = slot.TalkId %}
{% assign content   = content_s | plus: 0 %}
{% if content != 0 %}
{% if content < 1000 %}
<hr style="width:50%;;margin-left:25%">
{% assign presentation_ = presentations | where: 'Submission ID', content_s %}
{% assign presentation  = presentation_[0] %}
### {{ presentation['Title'] | strip_newlines }}

T{{ slot.SlotId }} (sub. \#{{ presentation["Submission ID"] }}), {{ session.DayShort  }} at {{ slot.Start }}, in Gaston Berger.

By {% assign authors = presentation['Authors with Affiliations'] | replace: ' (BOSC)', ', BOSC' | replace: ' (', '**, ' | replace: '); ', '. **' | replace: ')', '.' -%}
**{{ authors }}

{% if presentation['Summary'] %}**Abstract**: {{ presentation['Summary'] }} {% endif %}

{% elsif content >= 1000 and content < 2000 %}
{% assign presentation_ = invited | where: 'SubmissId', content_s %}
{% assign presentation  = presentation_[0] %}
{% unless presentation.Status == "OnHold" %}
<hr style="width:50%;;margin-left:25%">
### {{ presentation['TalkTitle'] | strip_newlines }}

T{{ slot.SlotId }}, {{ session.DayShort  }} at {{ slot.Start }}, in Gaston Berger.

By **{{ presentation.FirstName | strip }} {{ presentation.LastName | strip }}**
{%- if presentation.Position -%}, {{ presentation.Position | strip }}{%- endif -%}
{%- if presentation.Company  -%}, {{ presentation.Company  | strip }}{%- endif -%}
.

{% if presentation.TalkAbstract %}**Abstract**: {{ presentation['TalkAbstract'] | strip_newlines }} {% endif %}

{% if presentation.Bio          %}**Bio**:     *{{ presentation['Bio'] | strip_newlines }}* {% endif %}
{% endunless %}
{% elsif content >= 2000 %}
{% assign panel_ = panels | where: 'SessionId', content_s %}
{% assign panel  = panel_[0] %}
{% unless presentation.Status == "OnHold" %}

## Panel -- {{ panel.Title }}

T{{ slot.SlotId }}, {{ session.DayShort  }} at {{ slot.Start }}, in
{% if session.Kind == "Breakfast" %}Louis Armand East{% else %}Gaston Berger{% endif %}.

Moderated by **{{ panel.ModerName }}**
{%- if panel.ModerPosition -%}, {{ panel.ModerPosition | strip }}{%- endif -%}
{%- if panel.ModerCompany  -%}, {{ panel.ModerCompany  | strip }}{%- endif -%}
.

{% if panel.Argument %}**Argument**: {{ panel.Argument | strip_newlines }} {% endif %}

{% endunless %}
{% endif %}
{% endif %}
{% endfor %}
{% endfor %}

{% include jumboboxend.html %}
