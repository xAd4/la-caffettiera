from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, UpdateView
from django.utils.decorators import method_decorator
from django.contrib.admin.views.decorators import staff_member_required
from django import forms
from .models import Store


# Método de seguridad - Solo usuarios administradores
class StaffIsRequiredMixin(object):
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super(StaffIsRequiredMixin, self).dispatch(request, *args, **kwargs)

# Create your views here.

class StoreTemplateView(TemplateView):
    template_name = "store/store.html"

# EDICIÓN DE STORE TEMPLATE

@method_decorator(staff_member_required, name="dispatch")
class StoreUpdateView(UpdateView):
    model = Store
    template_name = "forms/form_update.html"
    fields = ["title", "week_days", "week_days_schedule", "weekend", "weekend_schedule", "sunday", "sunday_schedule", "address", "city"]
    success_url = reverse_lazy("store")

    def get_form(self, form_class = None): 
        form = super(StoreUpdateView, self).get_form()
        form.fields["title"].widget = forms.TextInput(attrs={"class": "form-control mb-2", 'placeholder':"Título"})
        form.fields["week_days"].widget = forms.TextInput(attrs={"class": "form-control mb-2", 'placeholder':"Días de semana"})
        form.fields["week_days_schedule"].widget = forms.TextInput(attrs={"class": "form-control mb-2", 'placeholder':"Horario de días de semana"})
        form.fields["weekend"].widget = forms.TextInput(attrs={"class": "form-control mb-2", 'placeholder':"Fines de semana"})
        form.fields["weekend_schedule"].widget = forms.TextInput(attrs={"class": "form-control mb-2", 'placeholder':"Horario de fines de semana"})
        form.fields["sunday"].widget = forms.TextInput(attrs={"class": "form-control mb-2", 'placeholder':"Domingos"})
        form.fields["sunday_schedule"].widget = forms.TextInput(attrs={"class": "form-control mb-2", 'placeholder':"Horario de los Domingos"})
        form.fields["address"].widget = forms.TextInput(attrs={"class": "form-control mb-2", 'placeholder':"Dirección"})
        form.fields["city"].widget = forms.TextInput(attrs={"class": "form-control mb-2", 'placehold          er':"Ciudad"})
        return form
