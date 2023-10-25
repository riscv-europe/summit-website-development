### {{ poster["First Name"] }} {{ poster["Last Name"]}} -- {{ poster["Paper Title"] | strip_newlines }}

{% assign org = poster["Organization"] %}
{% if org %}{% assign org = org | append: ", " | append: poster["Primary Address - City"]%}{% else %}{% assign org = poster["Primary Address - City"]%}{% endif %}
{% if org %}{% assign org = org | append: ", " | append: poster["Primary Address - Country"]%}{% else %}{% assign org = poster["Primary Address - Country"]%}{% endif %}
{{ poster["First Name"] }} {{ poster["Last Name"]}} {% if org %}({{ org }}){% endif %}{% if poster["Rest of the authors"] %}, {{ poster["Rest of the authors"] }}{% endif %}

*Poster #{{ poster["Poster board"] }} in {{ poster["MR"] }}*
*on {% case poster["Day (Poster)"] %}{% when "Tue" %}Tue 6th{% endcase %}{% if poster["HasAbstract"] %}, [extended abstract](media/proceedings/posters/{{poster["BaseFileName"]}}-abstract.pdf){% endif %}{% if poster["HasPoster"] %}, [poster](media/proceedings/posters/{{poster["BaseFileName"]}}-poster.pdf){% endif %}.*

{% if poster["Final abstract"] %}
**Summary**

{{ poster["Final abstract"] }}
{% endif %}

{% if poster["Bio"] %}
*Bio*

{{ poster["Bio"] }}
{% endif %}

