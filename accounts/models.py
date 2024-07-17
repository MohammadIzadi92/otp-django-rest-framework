from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from .validators import PhoneNumberValidator
from .managers import CustomUserManager


class CustomUser(AbstractUser):
    phone_number_validator = PhoneNumberValidator()
    
    phone_number = models.CharField(max_length=20, validators=[phone_number_validator], unique=True, blank=True, null=True)
    username = models.CharField(max_length=150)

    objects = CustomUserManager()
    USERNAME_FIELD = "phone_number"
        
    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")
    
    def __str__(self) -> str:
        return self.user()
    
    def user(self):
        return f"User {self.pk}"
