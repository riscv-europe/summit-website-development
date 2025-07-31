{% if talk['TalkTitle'] %}

<h3 id="{{ talk['FirstName'] }}-{{ talk['LastName'] }}-talk">{{ talk['TalkTitle'] }}</h3>

<p style="font-size: 80%;">
{%- if slot['YouTubeURL'] %}<a href="media/proceedings/{{ slot['YouTubeURL'] }}" style="display: inline-flex; align-items: center; line-height: normal;">Video&nbsp;<img style="height: 1em; width: auto; vertical-align: middle; display: inline-block;" src="media/logos/inline-youtube-logo.svg" alt="YouTube icon"/></a>. {% endif -%}
{%- if slot['AbstractPDFFileName'] %}<a href="media/proceedings/{{ slot['AbstractPDFFileName'] }}" style="display: inline-flex; align-items: center; line-height: normal;">Extended abstract&nbsp;<img style="height: 1em; width: auto; vertical-align: middle; display: inline-block;" src="media/logos/inline-pdf-logo.svg" alt="PDF icon"/></a>. {% endif -%}
{%- if slot['SlidesPDFFileName'] %}<a href="media/proceedings/{{ slot['SlidesPDFFileName'] }}" style="display: inline-flex; align-items: center; line-height: normal;">Slides&nbsp;<img style="height: 1em; width: auto; vertical-align: middle; display: inline-block;" src="media/logos/inline-pdf-logo.svg" alt="PDF icon"/></a>. {% endif -%}
{%- if slot['PosterPDFFileName'] %}<a href="media/proceedings/{{ slot['PosterPDFFileName'] }}" style="display: inline-flex; align-items: center; line-height: normal;">Poster&nbsp;<img style="height: 1em; width: auto; vertical-align: middle; display: inline-block;" src="media/logos/inline-pdf-logo.svg" alt="PDF icon"/></a>. {% endif -%}
T{{ slot.SlotId }}, {{ session.DayLong }} at {{ slot.Start }}, in Gaston Berger amphitheater (S2).
</p>

By **{{ talk['FirstName'] }} {{ talk['LastName'] }}**
{%- if talk['Position'] -%}, {{ talk['Position'] | strip }} {%- endif -%}
{%- if talk['Company']  -%}, {{ talk['Company']  | strip }} {%- endif -%}
.

{% if talk['TalkAbstract'] %}**Abstract**: {{ talk['TalkAbstract'] | strip_newlines }} {% endif %}

{% if talk['Bio']          %}**Bio**:     *{{ talk['Bio'] | strip_newlines }}* {% endif %}

{% endif %}
