from django.template import Library

register = Library()


@register.filter(name="format_date")
def format_date(value):
    return value.strftime("%B %d, %Y")
