from django import template
import datetime

register = template.Library()


@register.filter(expects_localtime=True)
def parse_date(value):
    return datetime.datetime.strptime(value, "%Y-%m-%dT%H:%M:%SZ")
