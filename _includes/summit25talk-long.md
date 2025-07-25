{% if talk['TalkTitle'] %}

<h3 id="{{ talk['FirstName'] }}-{{ talk['LastName'] }}-talk">{{ talk['TalkTitle'] }}</h3>

{% if slot['YouTubeURL'] %}<a href="{{ slot['YouTubeURL'] }}" style="display: inline-flex; align-items: center; line-height: normal;">Video&nbsp;<img style="height: 1em; width: auto; vertical-align: middle; display: inline-block;" src="media/logos/inline-youtube-logo.svg" alt="YouTube icon"/></a>.{% endif %}
T{{ slot.SlotId }}, {{ session.DayLong }} at {{ slot.Start }}, in Gaston Berger amphitheater (S2).

By **{{ talk['FirstName'] }} {{ talk['LastName'] }}**
{%- if talk['Position'] -%}, {{ talk['Position'] | strip }} {%- endif -%}
{%- if talk['Company']  -%}, {{ talk['Company']  | strip }} {%- endif -%}
.

{% if talk['TalkAbstract'] %}**Abstract**: {{ talk['TalkAbstract'] | strip_newlines }} {% endif %}

{% if talk['Bio']          %}**Bio**:     *{{ talk['Bio'] | strip_newlines }}* {% endif %}

{% endif %}
