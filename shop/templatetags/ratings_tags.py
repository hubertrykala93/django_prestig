from django import template

register = template.Library()


@register.filter(name="to_star_range")
def to_star_range(value):
    return range(1, 6)
