from django.template import Library

register = Library()


@register.filter(name="lower")
def lower(value):
    return value.lower()
