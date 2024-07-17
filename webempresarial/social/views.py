from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from django import forms
from django.utils.decorators import method_decorator
from django.contrib.admin.views.decorators import staff_member_required
from .models import Social

# Create your views here.

###################################################################################################################

# Método de seguridad - Solo usuarios administradores pueden manipular las opciones CRUD
class StaffIsRequiredMixin(object):
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super(StaffIsRequiredMixin, self).dispatch(request, *args, **kwargs)

# Implementación CRUD del método 'SOCIAL' solo para uso de administradores

###################################################################################################################

@method_decorator(staff_member_required, name="dispatch")
class SocialCreateView(CreateView): # Crear instancias
    model = Social
    template_name = "forms/form_create.html"
    fields = ["name", "url"]
    success_url = reverse_lazy("home")

    def get_form(self, form_class = None): 
        form = super(SocialCreateView, self).get_form()
        form.fields["name"].widget = forms.TextInput(attrs={"class": "form-control mb-2", 'placeholder':"Título"})
        form.fields["url"].widget = forms.TextInput(attrs={"class": "form-control mb-2", 'placeholder':"URL"})
        return form
    
###################################################################################################################

@method_decorator(staff_member_required, name="dispatch")
class SocialUpdateView(UpdateView): # Actualizar instancias
    model = Social
    template_name = "forms/form_update.html"
    fields = ["name", "url"]
    success_url = reverse_lazy("home")

    def get_form(self, form_class = None): 
        form = super(SocialUpdateView, self).get_form()
        form.fields["name"].widget = forms.TextInput(attrs={"class": "form-control mb-2", 'placeholder':"Título"})
        form.fields["url"].widget = forms.TextInput(attrs={"class": "form-control mb-2", 'placeholder':"URL"})
        return form

###################################################################################################################

@method_decorator(staff_member_required, name="dispatch")
class SocialDeleteView(DeleteView): # Borrar instancias
    model = Social
    template_name = "forms/form_confirm_delete.html"
    success_url = reverse_lazy("home")
