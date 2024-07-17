from django import template
from sample.models import Sample

register = template.Library()

@register.simple_tag
def get_sample_list():
    sample = Sample.objects.all()
    return sample