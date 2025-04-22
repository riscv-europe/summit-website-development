{% assign islands = site.data.islands-config | where: 'Day', day %}
{% assign stands  = site.data.posters-agenda | where: 'Day', day %}

{% for island in islands %}

{% assign standsOfIsland = stands | where: 'Island', island.Island %}

{% unless standsOfIsland.size == 0 %}

<hr>
<p align="center" style="font-weight: bold; font-size: 1.875em">On {{ dayLong }}, at island {{ island.Island }} (level {{ island.Level }})</p>

{% for stand in standsOfIsland %}

{% assign submissId = stand.PosterId | plus: 0 %}

{% unless submissId == 0 %}

{% assign poster_ = posters | where: 'Submission ID', submissId %}
{% assign poster  = poster_[0] %}

### {{ poster["Title"] | strip_newlines }}

P{{ stand.StandId }} (sub. \#{{ poster['Submission ID'] }}). On {{ dayLong }}, at island {{ island.Island }} on level {{island.Level }}.

**{{ poster["Main Contact Firstname"] }} {{ poster["Main Contact Lastname"]}}**, {{ poster["Main Contact Affiliation"] }}.

{% if poster['Summary'] %}**Abstract**: {{ poster['Summary'] }} {% endif %}

<p><i>Back to <a href="#summary">posters' summary</a>, or <a href="#{{ day }}">{{ dayLong }} posters</a>.</i></p>

{% endunless %}

{% endfor %}

{% endunless %}

{% endfor %}
