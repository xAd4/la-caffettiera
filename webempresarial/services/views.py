from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Service
from django import forms
from django.utils.decorators import method_decorator
from django.contrib.admin.views.decorators import staff_member_required

# Método de seguridad - Solo usuarios administradores pueden manipular las opciones CRUD
class StaffIsRequiredMixin(object):
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super(StaffIsRequiredMixin, self).dispatch(request, *args, **kwargs)

# Create your views here.

class ServiceListView(ListView): # Muestra lista de instancias del módelo "SERVICIOS"
    model = Service
    template_name = "services/services.html"

# Implementación CRUD del método 'SAMPLE' solo para uso de administradores

###################################################################################################################

@method_decorator(staff_member_required, name="dispatch") 
class ServiceCreateView(CreateView): # Crear nueva instancia del modelo "SERVICIO"
    model = Service
    template_name = "forms/form_create.html"
    fields = ["title", "subTitle", "content", "image"]
    success_url = reverse_lazy("services")

    def get_form(self, form_class = None): 
        form = super(ServiceCreateView, self).get_form()
        form.fields["title"].widget = forms.TextInput(attrs={"class": "form-control mb-2", 'placeholder':"Título"})
        form.fields["subTitle"].widget = forms.TextInput(attrs={"class": "form-control mb-2", 'placeholder':"Subtítulo"})
        form.fields["content"].widget = forms.Textarea(attrs={"class": "form-control mb-2", 'placeholder':"Contenido"})
        form.fields["image"].widget = forms.ClearableFileInput()
        return form


###################################################################################################################

@method_decorator(staff_member_required, name="dispatch")
class ServiceUpdateView(UpdateView): # Actualiza una instancia del modelo "SERVICIO"
    model = Service
    template_name = "forms/form_update.html"
    fields = ["title", "subTitle", "content", "image"]
    success_url = reverse_lazy("services")
    
    def get_form(self, form_class = None): 
        form = super(ServiceUpdateView, self).get_form()
        form.fields["title"].widget = forms.TextInput(attrs={"class": "form-control mb-2", 'placeholder':"Título"})
        form.fields["subTitle"].widget = forms.TextInput(attrs={"class": "form-control mb-2", 'placeholder':"Subtítulo"})
        form.fields["content"].widget = forms.Textarea(attrs={"class": "form-control mb-2", 'placeholder':"Contenido"})
        form.fields["image"].widget = forms.ClearableFileInput(attrs={"class": "form-control mb-2"})
        return form


###################################################################################################################

@method_decorator(staff_member_required, name="dispatch")
class ServiceDeleteView(DeleteView): # Borra una instancia del modelo "SERVICIO"
    model = Service
    template_name = "forms/form_confirm_delete.html"
    success_url = reverse_lazy("services")

