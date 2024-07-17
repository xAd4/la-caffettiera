from django import template
from contact.models import Contact

register = template.Library()

@register.simple_tag
def get_contact_list():
    contact = Contact.objects.all()
    return contact