from django.template import Library
from django.utils.html import strip_tags
from django.utils.safestring import mark_safe
import html

register = Library()


# @register.filter(name="truncate_and_safe")
# def truncate_and_safe(value):
#     print(f"Original value -> {value}")
#     truncated_value = strip_tags(value)[:100]
#     print(f"Truncated value -> {truncated_value}")
#
#     return mark_safe(truncated_value)

@register.filter(name="truncate_and_safe")
def truncate_and_safe(value):
    decoded_value = html.unescape(s=value)
    truncated_value = strip_tags(decoded_value)[:100]

    return mark_safe(truncated_value)

# @register.filter(name="safe_html")
# def safe_html(value):
#     decoded_value = html.unescape(s=value)
#     print(f"Original value -> {value}")
#     truncated_value = strip_tags(decoded_value)[:100]
#     print(f"Truncated value -> {truncated_value}")
#
#     return mark_safe(truncated_value)
