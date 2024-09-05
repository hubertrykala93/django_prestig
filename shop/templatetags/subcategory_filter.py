from django import template

register = template.Library()


@register.filter(name="remove_word")
def remove_word(value):
    return value.split(sep=" ")[-1]
