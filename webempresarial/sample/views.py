from django.urls import reverse_lazy
from django.views.generic import UpdateView, ListView, DetailView, CreateView, DeleteView
from django import forms
from django.utils.decorators import method_decorator
from django.contrib.admin.views.decorators import staff_member_required
from .models import Sample

# Create your views here.

###################################################################################################################

# Método de seguridad - Solo usuarios administradores pueden manipular las opciones CRUD
class StaffIsRequiredMixin(object):
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super(StaffIsRequiredMixin, self).dispatch(request, *args, **kwargs)

# Lista de instancias del modelo 'SAMPLE'
class SampleListView(ListView):
    model = Sample
    template_name = "sample/sample.html"

# Instancias detallas individualmente del modelo 'SAMPLE'
class SampleDetailView(DetailView):
    model = Sample
    template_name = "sample/sample_detail.html"

# Implementación CRUD del método 'SAMPLE' solo para uso de administradores

###################################################################################################################

@method_decorator(staff_member_required, name="dispatch")
class SampleCreateView(CreateView): # Crear instancias
    model = Sample
    template_name = "forms/form_create.html"
    fields = ["title", "content"]
    success_url = reverse_lazy("home")

    def get_form(self, form_class = None): 
        form = super(SampleCreateView, self).get_form()
        form.fields["title"].widget = forms.TextInput(attrs={"class": "form-control mb-2", 'placeholder':"Título"})
        form.fields["content"].widget = forms.Textarea(attrs={"class": "form-control mb-2", 'placeholder':"Contenido"})
        return form
    
###################################################################################################################

@method_decorator(staff_member_required, name="dispatch")
class SampleUpdateView(UpdateView): # Actualizar instancias
    model = Sample
    template_name = "forms/form_update.html"
    fields = ["title", "content"]
    success_url = reverse_lazy("home")

    def get_form(self, form_class = None): 
        form = super(SampleUpdateView, self).get_form()
        form.fields["title"].widget = forms.TextInput(attrs={"class": "form-control mb-2", 'placeholder':"Título"})
        form.fields["content"].widget = forms.Textarea(attrs={"class": "form-control mb-2", 'placeholder':"Contenido"})
        return form
    
###################################################################################################################

@method_decorator(staff_member_required, name="dispatch")
class SampleDeleteView(DeleteView): # Borrar instancias
    model = Sample
    template_name = "forms/form_confirm_delete.html"
    success_url = reverse_lazy("home")



