**{{ poster["Title"] | strip_newlines }}**

{% if poster.File %} <a href="media/proceedings/posters/{{ poster.File }}"><img src="/assets/icons/file-earmark-pdf.svg"> Poster</a>{% endif %}

{{ poster["Main Contact Firstname"] }} {{ poster["Main Contact Lastname"]}} ({{ poster["Main Contact Affiliation"] }})<br/>*Poster stand {{ poster["Stand"] }}*