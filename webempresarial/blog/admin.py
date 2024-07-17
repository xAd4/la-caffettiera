from django.contrib import admin
from .models import Category, Blog

# Register your models here.

class CategoryAndBlogAdmin(admin.ModelAdmin):
    readonly_fields = ("created_at", "updated_at")

admin.site.register(Category, CategoryAndBlogAdmin)
admin.site.register(Blog, CategoryAndBlogAdmin)
