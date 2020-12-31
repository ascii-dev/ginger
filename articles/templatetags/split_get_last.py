from django import template

register = template.Library()


@register.filter(expects_localtime=True)
def split_get_last(value, key):
    """
    Splits a string into an array and returns the last element of the array
    :param value: the string to split
    :param key: the separator to split by
    :return: the string at the last index in the array
    """
    return value.split(key)[-1]
