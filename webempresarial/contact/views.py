from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, UpdateView
from django.utils.decorators import method_decorator
from django.contrib.admin.views.decorators import staff_member_required
from django import forms
from .models import Contact

# Método de seguridad - Solo usuarios administradores
class StaffIsRequiredMixin(object):
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super(StaffIsRequiredMixin, self).dispatch(request, *args, **kwargs)

# Create your views here.
class ContactTemplateView(TemplateView):
    template_name = "contact/contact.html"

@method_decorator(staff_member_required, name="dispatch")
class ContactUpdateView(UpdateView):
    model = Contact
    template_name = "forms/form_update.html"
    fields = ["title", "email", "phone_number"]
    success_url = reverse_lazy("contact")

    def get_form(self, form_class = None): 
        form = super(ContactUpdateView, self).get_form()
        form.fields["title"].widget = forms.TextInput(attrs={"class": "form-control mb-2", 'placeholder':"Título"})
        form.fields["email"].widget = forms.TextInput(attrs={"class": "form-control mb-2", 'placeholder':"Email"})
        form.fields["phone_number"].widget = forms.TextInput(attrs={"class": "form-control mb-2", 'placeholder':"Número de teléfono"})
        return form

