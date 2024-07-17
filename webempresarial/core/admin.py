from django.contrib import admin
from .models import SectionOne, SectionTwo

# Register your models here.

class SectionAdmin(admin.ModelAdmin):
    readonly_fields = ("created_at", "updated_at")

admin.site.register(SectionOne, SectionAdmin)
admin.site.register(SectionTwo, SectionAdmin)
