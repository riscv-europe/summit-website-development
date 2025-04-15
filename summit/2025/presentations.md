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
    title = "Plenary sessions"
    lead =  "Keynotes, invited talks, industrial and technical presentations in the Gaston Berger amphitheater."
%}

{% assign presentations = site.data.summit25posters %}
{% assign invited = site.data.invited-slots-details %}
{% assign config  = site.data.plenary-sessions-config | sort_natural: SessionId %}
{% assign agenda  = site.data.plenary-sessions-agenda %}
{% for session in config %}
<hr>
## {{ session.DayLong }},  {{ session.Start }}-{{ session.End }}
{% assign sessionId = session.SessionId %}
{% assign block = agenda | where: 'PlenarySessionId', sessionId | sort_natural: TalkSessionId %}
{% for slot in block %}
{% assign content_s = slot['SubmissId'] %}
{% assign content   = slot['SubmissId'] | plus: 0 %}
{% if content != 0 %}
{% if content < 1000 %}
<hr style="width:50%;;margin-left:25%">
{% assign presentation_ = presentations | where: 'Submission ID', content_s %}
{% assign presentation  = presentation_[0] %}
### {{ presentation['Title'] | strip_newlines }}

P{{ slot["TalkSessionId"] }} (submission \#{{ slot.SubmissId }}), {{ session.DayShort  }} at {{ slot['TalkStartTime'] }}, in Gaston Berger.

By **{{ presentation["Main Contact Firstname"] | strip }} {{ presentation["Main Contact Lastname"] | strip }}**
{%- if presentation['Main Contact Job Function'] -%}, {{ presentation['Main Contact Job Function'] | strip }}{%- endif -%}
{%- if presentation['Main Contact Affiliation']  -%}, {{ presentation["Main Contact Affiliation"]  | strip }}{%- endif -%}
.

{% elsif content >= 1000 and content < 2000 %}
<hr style="width:50%;;margin-left:25%">
{% assign presentation_ = invited | where: 'SubmissId', content_s %}
{% assign presentation  = presentation_[0] %}
### {{ presentation['TalkTitle'] | strip_newlines }}

P{{ slot["TalkSessionId"] }}, {{ session.DayShort  }} at {{ slot['TalkStartTime'] }}, in Gaston Berger.

By **{{ presentation.FirstName | strip }} {{ presentation.LastName | strip }}**
{%- if presentation.Position -%}, {{ presentation.Position | strip }}{%- endif -%}
{%- if presentation.Company  -%}, {{ presentation.Company  | strip }}{%- endif -%}
.

{% else %}
Panel
{% endif %}
{% endif %}
{% endfor %}
{% endfor %}

{% include jumboboxend.html %}
