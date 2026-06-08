
{% assign posters_ = posters | where: 'Day', day  %}

{% for poster in posters_ %}

<hr style="width:50%;;margin-left:25%">
<h3 id="P-{{  }}">{{ poster['Title'] | strip | strip_newlines }}</h3>

{{ poster['Blindness'] }} submission #{{ poster['Id'] }} at poster <strong>island {{ poster['Island']}}/{{ poster['Slot']}}</strong> on {{ dayLong }}.

{% if poster['Authors'] %}{{ poster['Authors'] }}.{% endif %}

{% if poster['Abstract'] %}**Abstract**: {{ poster['Abstract'] }} {% endif %}

{% if poster['Bio'] %}**Bio**: *{{ poster['Bio'] }}* {% endif %}

<p align="center" style="font-size: 0.8em">
<a class="backnavigation" href="#summary">To page top</a> &mdash;
<a href="#Tue" class="backnavigation">To posters of Tuesday 9</a> &mdash;
<a href="#Wed" class="backnavigation">To posters of Wednesday 10</a> &mdash;
<a href="#Thu" class="backnavigation">To posters of Thursday 11</a>
</p>

{% endfor %}
