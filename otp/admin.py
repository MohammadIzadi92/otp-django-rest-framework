from django.contrib import admin
from .models import OTPRequest


@admin.register(OTPRequest)
class OTPRequestAdmin(admin.ModelAdmin):
    pass
