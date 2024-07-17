from django.views.generic import TemplateView, UpdateView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.admin.views.decorators import staff_member_required
from django import forms
from .models import SectionOne, SectionTwo

# Método de seguridad - Solo usuarios administradores pueden manipular las opciones CRUD
class StaffIsRequiredMixin(object):
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super(StaffIsRequiredMixin, self).dispatch(request, *args, **kwargs)
    
###################################################################################################################

# Create your views here.
class HomeTemplateView(TemplateView): # TemplateView de la página principal
    template_name = "core/index.html"

###################################################################################################################    

@method_decorator(staff_member_required, name="dispatch")
class HomeCoreOneUpdateView(UpdateView): # Edición del artículo uno.
    model = SectionOne
    template_name = "forms/form_update.html"
    fields = ["title", "subTitle", "content"]
    success_url = reverse_lazy("home")

    def get_form(self, form_class = None): 
        form = super(HomeCoreOneUpdateView, self).get_form()
        form.fields["title"].widget = forms.TextInput(attrs={"class": "form-control mb-2", 'placeholder':"Título"})
        form.fields["subTitle"].widget = forms.TextInput(attrs={"class": "form-control mb-2", 'placeholder':"Contenido"})
        form.fields["content"].widget = forms.Textarea(attrs={"class": "form-control mb-2", 'placeholder':"Contenido"})
        return form

###################################################################################################################
 
@method_decorator(staff_member_required, name="dispatch")
class HomeCoreTwoUpdateView(UpdateView): # Edición del artículo dos.
    model = SectionTwo
    template_name = "forms/form_update.html"
    fields = ["title", "subTitle", "content"]
    success_url = reverse_lazy("home")

    def get_form(self, form_class = None): 
        form = super(HomeCoreTwoUpdateView, self).get_form()
        form.fields["title"].widget = forms.TextInput(attrs={"class": "form-control mb-2", 'placeholder':"Título"})
        form.fields["subTitle"].widget = forms.TextInput(attrs={"class": "form-control mb-2", 'placeholder':"Contenido"})
        form.fields["content"].widget = forms.Textarea(attrs={"class": "form-control mb-2", 'placeholder':"Contenido"})
        return form

###################################################################################################################
