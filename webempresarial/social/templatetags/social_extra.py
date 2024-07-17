from django import template
from social.models import Social

register = template.Library()

@register.simple_tag
def get_social_list():
    social = Social.objects.all()
    return social