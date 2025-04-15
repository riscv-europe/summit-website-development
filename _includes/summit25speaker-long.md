{% if speaker['TalkTitle'] %}

<h3 id="{{ speaker['FirstName'] }}-{{ speaker['LastName'] }}-talk">{{ speaker['TalkTitle'] }}</h3>

P{{ slot.TalkSessionId }}, {{ day.DayLong }} at {{ slot.TalkStartTime }}, in Gaston Berger amphitheater.

By **{{ speaker['FirstName'] }} {{ speaker['LastName'] }}**
{%- if speaker['Company']  -%}, {{ speaker['Company']  | strip }} {%- endif -%}
{%- if speaker['Position'] -%}, {{ speaker['Position'] | strip }} {%- endif -%}
.

{% if speaker['TalkAbstract'] %}**Abstract**: {{ speaker['TalkAbstract'] }} {% endif %}

{% if speaker['Bio']          %}**Bio**:     *{{ speaker['Bio'] | strip_newlines }}* {% endif %}

{% endif %}
