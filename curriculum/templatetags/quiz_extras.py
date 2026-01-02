from django import template

register = template.Library()

@register.filter
def get_option(quiz, option_number):
    """
    Returns option_1, option_2, etc., dynamically based on number.
    Usage: {{ quiz|get_option:'1' }}
    """
    field_name = f"option_{option_number}"
    return getattr(quiz, field_name, None)
