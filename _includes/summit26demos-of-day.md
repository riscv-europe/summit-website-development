
{% assign demos_ = demos | where: 'Day', day | sort: 'Time' %}

{% for demo in demos_ %}

<hr style="width:50%;;margin-left:25%">
<h3 id="P-{{  }}">{{ demo['Title'] | strip | strip_newlines }}</h3>

{%- if demo['Room'] %}Academic demo in **{{ demo['Room'] }}**. {% endif -%}
On {{ dayLong }}, at **{{ demo['Time'] }}**.

{% if demo['Authors'] %}{{ demo['Authors'] }}.{% endif %}

{% if demo['Abstract'] %}**Abstract**: {{ demo['Abstract'] }} {% endif %}
<p align="center" style="font-size: 0.8em">
<a class="backnavigation" href="#summary">To page top</a> &mdash;
<a href="#Tue" class="backnavigation">To demos of Tuesday 9</a> &mdash;
<a href="#Wed" class="backnavigation">To demos of Wednesday 10</a> &mdash;
<a href="#Thu" class="backnavigation">To demos of Thursday 11</a>
</p>

{% endfor %}
