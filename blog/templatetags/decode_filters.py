from django.template import Library
from urllib.parse import unquote

register = Library()


@register.filter(name="decode")
def decode(value):
    return unquote(string=value)
