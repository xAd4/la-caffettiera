from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django import forms
from django.utils.decorators import method_decorator
from django.contrib.admin.views.decorators import staff_member_required
from .models import Blog, Category

# Método de seguridad - Solo usuarios administradores pueden manipular las opciones CRUD
class StaffIsRequiredMixin(object):
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super(StaffIsRequiredMixin, self).dispatch(request, *args, **kwargs)

# Create your views here.

# TODAS LAS INSTANCIAS DEL MODELO "BLOG"

class BlogListView(ListView):
    model = Blog
    template_name = "blog/blog.html"

# UNA INSTANCIA DEL MODELO "BLOG"
class BlogDetailView(DetailView):
    model = Blog
    template_name = "blog/blog_detail.html"

# Implementación CRUD del método 'BLOG' solo para uso de administradores

###################################################################################################################

@method_decorator(staff_member_required, name="dispatch")
class BlogCreateView(CreateView): # CREACIÓN DE INSTANCIAS DEL MODELO BLOG
    model = Blog
    template_name = "forms/form_create.html"
    fields = ["title", "image", "content", "author", "categories"]
    success_url = reverse_lazy("blog")

    def get_form(self, form_class = None): 
        form = super(BlogCreateView, self).get_form()
        form.fields["title"].widget = forms.TextInput(attrs={"class": "form-control mb-2", 'placeholder':"Título"})
        form.fields["image"].widget = forms.ClearableFileInput()
        form.fields["content"].widget = forms.Textarea(attrs={"class": "form-control mb-2", 'placeholder':"Contenido"})
        return form

###################################################################################################################

@method_decorator(staff_member_required, name="dispatch")
class BlogUpdateView(UpdateView): # ACTUALIZACIÓN DE UNA INSTANCIA DEL MODELO BLOG
    model = Blog
    template_name = "forms/form_update.html"
    fields = ["title", "image", "content", "categories"]
    success_url = reverse_lazy("blog")

    def get_form(self, form_class = None): 
        form = super(BlogUpdateView, self).get_form()
        form.fields["title"].widget = forms.TextInput(attrs={"class": "form-control mb-2", 'placeholder':"Título"})
        form.fields["image"].widget = forms.ClearableFileInput(attrs={"class": "form-control mb-2"})
        form.fields["content"].widget = forms.Textarea(attrs={"class": "form-control mb-2", 'placeholder':"Contenido"})
        return form

###################################################################################################################

@method_decorator(staff_member_required, name="dispatch")
class BlogDeleteView(DeleteView): # BORRAR UNA INSTANCIA DEL MODELO BLOG
    model = Blog
    template_name = "forms/form_confirm_delete.html"
    success_url = reverse_lazy("blog")


### CONTROL DE CATEGORIES
"""
.
.
"""

# CREACIÓN DE CATEGORÍAS

@method_decorator(staff_member_required, name="dispatch")
class CategoryListView(ListView):
    model = Category
    template_name = "blog/categories/categories.html"

###################################################################################################################

# Implementación CRUD del método 'CATEGORY' solo para uso de administradores

@method_decorator(staff_member_required, name="dispatch")
class CategoryCreateView(CreateView): # CREACIÓN DE INSTANCIAS DEL MODELO CATEGORY
    model = Category
    template_name = "forms/form_create.html"
    fields = ["name"]
    success_url = reverse_lazy("blog")

    def get_form(self, form_class = None): 
        form = super(CategoryCreateView, self).get_form()
        form.fields["name"].widget = forms.TextInput(attrs={"class": "form-control mb-2", 'placeholder':"Nombre de la categoría"})
        return form

###################################################################################################################

@method_decorator(staff_member_required, name="dispatch")
class CategoryUpdateView(UpdateView): # ACTUALIZACIÓN DE UNA INSTANCIA DEL MODELO CATEGORY
    model = Category
    template_name = "forms/form_update.html"
    fields = ["name"]
    success_url = reverse_lazy("blog")

    def get_form(self, form_class = None): 
        form = super(CategoryUpdateView, self).get_form()
        form.fields["name"].widget = forms.TextInput(attrs={"class": "form-control mb-2", 'placeholder':"Nombre de la categoría"})
        return form

###################################################################################################################

@method_decorator(staff_member_required, name="dispatch")
class CategoryDeleteView(DeleteView): # BORRAR UNA INSTANCIA DEL MODELO CATEGORY
    model = Category
    template_name = "forms/form_confirm_delete.html"
    success_url = reverse_lazy("blog")

