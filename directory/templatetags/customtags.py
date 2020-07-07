from django import template

register = template.Library()

@register.filter
def modulo(num, val):
    return num % val

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)
