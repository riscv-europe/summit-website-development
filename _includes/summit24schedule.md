{% assign program=site.data.summit24schedule | where: "day", include.day_id %}

<div class="schedule-day" id="top-{{ include.day_id }}">{{ include.day }}</div>

{% assign blocks = program | map, "blocktime" | uniq %}

{% for block in blocks %}
{% assign talks = program | where, "blocktime", block %}

<div class="schedule-block-title {{ talks[0]["type"] }}">
  <span class="schedule-block-time">{{ block }}</span><br/><span class="schedule-block-name">{{ talks[0]["blocktitle"] }}</span>
</div>

<div class="schedule-block">
{% for talk in talks %}
<div class="schedule-entry">
{% if talk.time %}<span class="schedule-time">{{ talk.time }}</span> - {% endif %}<span class="schedule-title">{{ talk.title }}</span>{% if talk.name %} - <span class="schedule-author">{{ talk.name }}</span>{% endif %}<br/>
</div>
{% endfor %}
</div>


{% endfor %}
