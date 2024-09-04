from django import template

register = template.Library()


@register.filter(name="convert_to_str")
def convert_to_str(value):
    return str(value)
