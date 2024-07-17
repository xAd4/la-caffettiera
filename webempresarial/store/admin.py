from django.contrib import admin
from .models import Store

# Register your models here.

class StoreAdmin(admin.ModelAdmin):
    readonly_fields = ("weekend","sunday","created_at", "updated_at")

admin.site.register(Store, StoreAdmin)
