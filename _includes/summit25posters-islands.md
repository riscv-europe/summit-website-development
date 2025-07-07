{% assign islands = site.data.summit2025.asimported.islands-config | where: 'Day', day %}
{% assign stands  = site.data.summit2025.integrated.posters-agenda | where: 'Day', day %}
{% assign levels  = "S1, S2, S3" | split: ", " -%}

 - {{ dayLong }}.
{%- for level in levels -%}
{%- assign hadPreviousIsland = false -%}
&#32; At {{ level }}: islands&#32;
{%- for island in islands -%}
{%- assign standsOfIsland = stands | where: 'Island', island.Island -%}
{%- unless island.Level != level or standsOfIsland.size == 0 -%}
{%- if hadPreviousIsland -%}
,&#32;
{%- endif -%}
<a href="#P{{ island.Island }}-{{ day }}">P{{ island.Island }}</a>
{%- assign hadPreviousIsland = true -%}
{%- endunless -%}
{%- endfor -%}
.
{%- endfor -%}
