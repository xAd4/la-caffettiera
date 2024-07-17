from django.contrib import admin
from .models import About

# Register your models here.

class AboutAdmin(admin.ModelAdmin):
    readonly_fields = ("created_at", "updated_at")

admin.site.register(About, AboutAdmin)
