{% if speaker['TalkTitle'] %}

<h3 id="{{ speaker['FirstName'] }}-{{ speaker['LastName'] }}-talk">{{ speaker['TalkTitle'] }}</h3>

By **{{ speaker['FirstName'] }} {{ speaker['LastName'] }}**, {{ speaker['Company'] }}, {{ speaker['Position'] }}.

{% if speaker['TalkAbstract'] %}Abstract: {{ speaker['TalkAbstract'] }}{% endif %}

{% if speaker['Bio'] %}Bio: *{{ speaker['Bio'] | strip_newlines }}* {% endif %}

{% endif %}
