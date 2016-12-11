from django import template

register = template.Library()

@register.filter(name='letter')
def letter(values, l):
    return values, l

@register.filter(name='number')
def number(values_l, n):
    """Finds the value in a dictionary"""
    values, l = values_l
    if values:
        return values[l + n]
    else:
        return ""
