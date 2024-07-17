from django import template
from core.models import SectionOne

register = template.Library()

@register.simple_tag
def get_coreone_list():
    core_one = SectionOne.objects.all()
    return core_one