
{% assign presentations_ = presentations | where: 'Day', day | sort: 'Time' %}

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

{% if presentation['Bio'] %}**Bio**: *{{ presentation['Bio'] }}* {% endif %}

<p align="center" style="font-size: 0.8em">
<a class="backnavigation" href="#summary">To page top</a> &mdash;
<a href="#Tue" class="backnavigation">To presentations of Tuesday 9</a> &mdash;
<a href="#Wed" class="backnavigation">To presentations of Wednesday 10</a> &mdash;
<a href="#Thu" class="backnavigation">To presentations of Thursday 11</a>
</p>

{% endfor %}
