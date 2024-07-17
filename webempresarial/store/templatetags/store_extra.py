from django import template
from store.models import Store

register = template.Library()

@register.simple_tag
def get_store_list():
    store = Store.objects.all()
    return store