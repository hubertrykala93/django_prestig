from django.template import Library
from django.utils.html import strip_tags
from django.utils.safestring import mark_safe

register = Library()


@register.filter(name="truncate_and_safe")
def truncate_and_safe(value):
    truncated_value = strip_tags(value)[:100]

    return mark_safe(truncated_value)
