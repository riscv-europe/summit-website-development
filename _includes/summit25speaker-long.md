{% if speaker['TalkTitle'] %}

<h3 id="{{ speaker['FirstName'] }}-{{ speaker['LastName'] }}-talk">{{ speaker['TalkTitle'] }}</h3>

{%- assign day = speaker['Session'] | strip | slice: 1,1 -%}
{%- assign ses = speaker['Session'] | strip | slice: 3,1 -%}

*Talk {{ speaker['Session'] | strip -}}
, part of plenary session starting at
**
{%- case ses -%}
{%- when '1' -%}
09h00
{%- when '2' -%}
11h30
{%- when '3' -%}
14h30
{%- else -%}
16h30
{%- endcase -%}
**
 on
**
{%- case day -%}
{%- when "1" -%}
Tuesday 13,
{%- when "2" -%}
Wednesday 14,
{%- else -%}
Thursday 15,
{%- endcase  -%}
**
 in **Gaston Berger** amphitheater.*

By **{{ speaker['FirstName'] }} {{ speaker['LastName'] }}**
{%- if speaker['Company']  -%}, {{ speaker['Company']  }} {%- endif -%}
{%- if speaker['Position'] -%}, {{ speaker['Position'] }} {%- endif -%}
.

{% if speaker['TalkAbstract'] %}Abstract: {{ speaker['TalkAbstract'] }} {% endif %}

{% if speaker['Bio']          %}Bio:     *{{ speaker['Bio'] | strip_newlines }}* {% endif %}

{% endif %}
