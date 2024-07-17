from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ("user", "phone_number", "email", "get_full_name")
    fieldsets = (
        (
            None,
            {
                "fields": ("phone_number", )
            }
        ),
    ) + UserAdmin.fieldsets
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide", ),
                "fields": ("first_name", "phone_number", "email") 
            }
        ),
    ) + UserAdmin.add_fieldsets
