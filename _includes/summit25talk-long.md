{% if talk['TalkTitle'] %}

<h3 id="{{ talk['FirstName'] }}-{{ talk['LastName'] }}-talk">{{ talk['TalkTitle'] }}</h3>

T{{ slot.SlotId }}, {{ session.DayLong }} at {{ slot.Start }}, in Gaston Berger amphitheater.

By **{{ talk['FirstName'] }} {{ talk['LastName'] }}**
{%- if talk['Position'] -%}, {{ talk['Position'] | strip }} {%- endif -%}
{%- if talk['Company']  -%}, {{ talk['Company']  | strip }} {%- endif -%}
.

{% if talk['TalkAbstract'] %}**Abstract**: {{ talk['TalkAbstract'] | strip_newlines }} {% endif %}

{% if talk['Bio']          %}**Bio**:     *{{ talk['Bio'] | strip_newlines }}* {% endif %}

{% endif %}
