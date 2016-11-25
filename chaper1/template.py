#! /usr/bin/python
# -*- coding:utf-8 -*-

import datetime

from django.template import Template, Context

raw_template = """
<p>Dear {{ person_name }},</p>
<p>Thanks for placing an order from {{ company }}. It's scheduled to
ship on {{ ship_date|date:"F j, Y" }}.</p>
{% if ordered_warranty %}
<p>Your warranty information will be included in the packaging.</p>
{% else %}
<p>You didn't order a warranty, so you're on your own when
the products inevitably stop working.</p>
{% endif %}
<p>Sincerely,<br />{{ company }}</p>"""
t = Template(raw_template)

c = Context({'person_name': 'houxiurong', 'company': 'Ngari Health',
             'ship_date': datetime.date(2016, 11, 25),
             'ordered_warranty': False})
t.render(c)
