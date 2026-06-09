
{% assign presentations_ = presentations | where: 'Day', day | sort: 'Time' %}

<div class="schedule">
{% assign current_type = "" %}
{% for presentation in presentations_ %}
{% if presentation['Type'] != current_type %}
{% unless forloop.first %}
</div>
{% endunless %}
{% assign current_type = presentation['Type'] %}
{% case presentation['Type'] %}
{% when 'keynote' %}{% assign blockclass = 'keynote' %}{% assign blockname = 'Keynotes' %}
{% when 'invited talk' %}{% assign blockclass = 'keynote' %}{% assign blockname = 'Invited talks' %}
{% when 'panel' %}{% assign blockclass = 'technical' %}{% assign blockname = 'Panels' %}
{% when 'steering' %}{% assign blockclass = 'org' %}{% assign blockname = "Events" %}
{% when 'demo_theater' %}{% assign blockclass = 'social' %}{% assign blockname = 'Demo theater' %}
{% else %}{% assign blockclass = 'technical' %}{% assign blockname = 'Talks' %}
{% endcase %}
<div class="schedule-block-title {{ blockclass }}">
<span class="schedule-block-time">{{ presentation['Time'] }}</span><br/><span class="schedule-block-name">{{ blockname }}</span>
</div>
<div class="schedule-block">
{% endif %}
<div class="schedule-entry">
{% if presentation['Time'] %}<span class="schedule-time">{{ presentation['Time'] }}</span> - {% endif %}<span class="schedule-title">{{ presentation['Title'] | strip | strip_newlines }}</span>{% if presentation['Authors'] %} - <span class="schedule-author">{{ presentation['Authors'] }}</span>{% endif %} <a href="#P-{{ presentation['Id'] }}"><img src="/assets/icons/card-text.svg"> Details</a>
</div>
{% endfor %}
</div>
</div>

{% for presentation in presentations_ %}

<hr style="width:50%;;margin-left:25%">
<h3 id="P-{{ presentation['Id'] }}">{{ presentation['Title'] | strip | strip_newlines }}</h3>

{%- if presentation['Type'] == "talk" -%}{{ presentation['Blindness'] }} submission #{{ presentation['Id'] }} {% endif -%}
{%- if presentation['Type'] == "keynote" -%}Keynote {% endif -%}
{%- if presentation['Type'] == "steering" -%}Organizers' annoucement {% endif -%}
{%- if presentation['Type'] == "invited talk" -%}Invited talk {% endif -%}
{%- if presentation['Type'] == "panel" -%}Panel {% endif -%}
{%- if presentation['Room'] %} in **{{ presentation['Room'] }}**{% endif -%}.
On {{ dayLong }}, at **{{ presentation['Time'] }}**.

{% if presentation['Type'] == "panel" %}
{% if presentation['Modetaror'] %}Moderator: {{ presentation['Moderator'] }}.{% endif %}

{% if presentation['Panelists'] %}Panelists: {{ presentation['Penelists'] }}.{% endif %}
{% else %}
{% if presentation['Authors'] %}{{ presentation['Authors'] }}.{% endif %}
{% endif %}

{% if presentation['Abstract'] %}**Abstract**: {{ presentation['Abstract'] }} {% endif %}

{% if presentation['Bios'] %}

{% for bio in presentation['Bios'] %}**Bio**: *{{ bio }}*<br>{% endfor %}

{% endif %}

<p align="center" style="font-size: 0.8em">
<a class="backnavigation" href="#summary">To page top</a> &mdash;
<a href="#Tue" class="backnavigation">To presentations of Tuesday 9</a> &mdash;
<a href="#Wed" class="backnavigation">To presentations of Wednesday 10</a> &mdash;
<a href="#Thu" class="backnavigation">To presentations of Thursday 11</a>
</p>

{% endfor %}
