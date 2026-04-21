<h3 id="{{ speaker.FirstName }}-{{ speaker.LastName }}-talk">{{ talk.TalkTitle }}</h3>
{% if false %}
<p style="font-size: 80%;">
{%- if slot.YouTubeURL %}<a href="{{ slot.YouTubeURL }}" style="display: inline-flex; align-items: center; line-height: normal;">Video&nbsp;<img style="height: 1em; width: auto; vertical-align: middle; display: inline-block;" src="media/logos/inline-youtube-logo.svg" alt="YouTube icon"/></a>. {% endif -%}
{%- if slot.AbstractPDFFileName %}<a href="media/proceedings/{{ slot.AbstractPDFFileName }}" style="display: inline-flex; align-items: center; line-height: normal;">Extended abstract&nbsp;<img style="height: 1em; width: auto; vertical-align: middle; display: inline-block;" src="media/logos/inline-pdf-logo.svg" alt="PDF icon"/></a>. {% endif -%}
{%- if slot.SlidesPDFFileName %}<a href="media/proceedings/{{ slot.SlidesPDFFileName }}" style="display: inline-flex; align-items: center; line-height: normal;">Slides&nbsp;<img style="height: 1em; width: auto; vertical-align: middle; display: inline-block;" src="media/logos/inline-pdf-logo.svg" alt="PDF icon"/></a>. {% endif -%}
{%- if slot.PosterPDFFileName %}<a href="media/proceedings/{{ slot.PosterPDFFileName }}" style="display: inline-flex; align-items: center; line-height: normal;">Poster&nbsp;<img style="height: 1em; width: auto; vertical-align: middle; display: inline-block;" src="media/logos/inline-pdf-logo.svg" alt="PDF icon"/></a>. {% endif -%}
T{{ slot.SlotId }}, {{ session.DayLong }} at {{ slot.Start }}, in Gaston Berger amphitheater (S2).
</p>
{% endif %}

<p>By <strong>{{ speaker.FirstName }} {{ speaker.LastName }}</strong>
{%- if speaker.Position -%}, {{ speaker.Position | strip }} {%- endif -%}
{%- if speaker.Company  -%}, {{ speaker.Company  | strip }} {%- endif -%}
.</p>

{% if talk.TalkAbstract %}<p><strong>Abstract</strong>: {{ talk.TalkAbstract | strip_newlines }}</p>{% endif %}

{% if speaker.Bio %}<p><strong>Bio</strong>: <em>{{ speaker.Bio | strip_newlines }}</em></p>{% endif %}
