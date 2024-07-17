from django.contrib import admin
from .models import Social

# Register your models here.

class SocialAdmin(admin.ModelAdmin):
    readonly_fields = ("created_at", "updated_at")

admin.site.register(Social, SocialAdmin)
