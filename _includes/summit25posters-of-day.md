{% assign islands = site.data.summit2025.asimported.islands-config | where: 'Day', day %}
{% assign stands  = site.data.summit2025.integrated.posters-agenda | where: 'Day', day %}

{% for island in islands %}

{% assign standsOfIsland = stands | where: 'Island', island.Island %}

{% unless standsOfIsland.size == 0 %}

<hr>
<p id="P{{ island.Island }}-{{ day }}" align="center" style="font-weight: bold; font-size: 1.875em">On {{ dayLong }}, at island P{{ island.Island }} ({{ island.Level }})</p>

{% for stand in standsOfIsland %}

{% assign submissId = stand.PosterId | plus: 0 %}

{% unless submissId == 0 %}

{% assign poster_ = posters | where: 'Submission ID', submissId %}
{% assign poster  = poster_[0] %}

<hr style="width:50%;;margin-left:25%">
### {{ poster["Title"] | strip_newlines }}

<p style="font-size: 80%;">
{% if stand['PosterPDFFileName']   %}<a href="media/proceedings/{{ stand['PosterPDFFileName'] }}"   style="display: inline-flex; align-items: center; line-height: normal;">Poster&nbsp;
	<img style="height: 1em; width: auto; vertical-align: middle; display: inline-block;" src="media/logos/inline-pdf-logo.svg" alt="PDF icon"/></a>.{% endif %}
{% if stand['AbstractPDFFileName'] %}<a href="media/proceedings/{{ stand['AbstractPDFFileName'] }}" style="display: inline-flex; align-items: center; line-height: normal;">Extented abstract&nbsp;
	<img style="height: 1em; width: auto; vertical-align: middle; display: inline-block;" src="media/logos/inline-pdf-logo.svg" alt="PDF icon"/></a>.{% endif %}
Sub. #{{ poster['Submission ID'] }}.
{{ dayLong }}, at island {{ island.Island }} on {{ island.Level }}.
(P{{ stand.StandId }}).</p>

{% assign authors = poster['Authors with Affiliations'] | replace: ' (BOSC)', ', BOSC' | replace: ' (', '**, ' | replace: '); ', '. **' | replace: ')', '.' -%}
**{{ authors }}

{% if poster['Summary'] %}**Abstract**: {{ poster['Summary'] }} {% endif %}

<p align="center" style="font-size: 0.8em"><a class="backnavigation" href="#summary">To page top</a> &mdash; <a href="#P{{ island.Island }}-{{ day }}" class="backnavigation">To posters at P{{ island.Island }} ({{ island.Level }}) on {{ dayLong }}</a> &mdash; <a href="#{{ day }}" class="backnavigation">To all posters of {{ dayLong }}</a></p>

{% endunless %}

{% endfor %}

{% endunless %}

{% endfor %}
