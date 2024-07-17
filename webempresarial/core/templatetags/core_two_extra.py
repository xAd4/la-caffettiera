from django import template
from core.models import SectionTwo

register = template.Library()

@register.simple_tag
def get_coretwo_list():
    core_two = SectionTwo.objects.all()
    return core_two