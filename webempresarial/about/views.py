from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.admin.views.decorators import staff_member_required
from django.views.generic import TemplateView, UpdateView
from django import forms
from .models import About

# Método de seguridad - Solo usuarios administradores pueden manipular las opciones CRUD
class StaffIsRequiredMixin(object):
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super(StaffIsRequiredMixin, self).dispatch(request, *args, **kwargs)

# Create your views here.

class AboutTemplateView(TemplateView):
    template_name = "about/about.html"

@method_decorator(staff_member_required, name="dispatch")
class AboutUpdateView(UpdateView):
    model = About
    template_name = "forms/form_update.html"
    fields = ["title", "subTitle", "content", "image"]
    success_url = reverse_lazy("about")

    def get_form(self, form_class = None): 
        form = super(AboutUpdateView, self).get_form()
        form.fields["title"].widget = forms.TextInput(attrs={"class": "form-control mb-2", 'placeholder':"Título"})
        form.fields["subTitle"].widget = forms.TextInput(attrs={"class": "form-control mb-2", 'placeholder':"Subtítulo"})
        form.fields["content"].widget = forms.Textarea(attrs={"class": "form-control mb-2", 'placeholder':"Contenido"})
        form.fields["image"].widget = forms.ClearableFileInput()
        return form
