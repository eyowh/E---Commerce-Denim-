from django import template

register = template.Library()

@register.filter
def format_number(value):
    """
    Format number with Indonesian thousand separator (dot)
    Example: 1000000 -> 1.000.000
    """
    try:
        return "{:,.0f}".format(value).replace(',', '.')
    except (ValueError, TypeError):
        return value

@register.filter
def format_currency(value):
    """
    Format currency with Indonesian formatting
    Example: 1000000 -> Rp 1.000.000
    """
    try:
        return "Rp {:,.0f}".format(value).replace(',', '.')
    except (ValueError, TypeError):
        return f"Rp {value}"

@register.filter
def add(value, arg):
    """
    Add two numbers
    """
    try:
        return int(value) + int(arg)
    except (ValueError, TypeError):
        return value
