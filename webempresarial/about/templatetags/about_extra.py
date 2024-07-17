from django import template
from about.models import About

register = template.Library()

@register.simple_tag
def get_about_list():
    about = About.objects.all()
    return about