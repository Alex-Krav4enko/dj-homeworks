from django.template import Library

register = Library()


@register.simple_tag
def cell_bg(percent):
    if percent:
        percent_value = float(percent)
        return 'green' if percent_value < 0 else '#fcd3d3' if (1 < percent_value < 2) else '#f98c8c' if (2 <= percent_value < 5) else 'red' if (percent_value > 5) else 'white'
    else:
        return 'white'
