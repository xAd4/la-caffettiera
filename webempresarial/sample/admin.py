from django.contrib import admin
from .models import Sample

# Register your models here.
class SampleAdmin(admin.ModelAdmin):
    readonly_fields = ("created_at", "updated_at")

admin.site.register(Sample, SampleAdmin)
