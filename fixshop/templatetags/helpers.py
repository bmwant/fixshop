# -*- coding: utf-8 -*-
__author__ = 'Most Wanted'
from django.template import Library
import logging
register = Library()


@register.filter(name='get_range')
def get_range(value):
    """
    {% for i in 3|get_range %}
        <li>{{ i }}. Do something</li>
      {% endfor %}
    """
    return range(value)

@register.filter(name='count')
def count(value):
    """
    attribute error
    """
    logging.debug(value)
    return value.count()