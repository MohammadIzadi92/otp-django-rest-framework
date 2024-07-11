from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from .validators import PhoneNumberValidator
from .managers import CustomUserManager

# Create your models here.


class CustomUser(AbstractBaseUser, PermissionsMixin):
    phone_number_validator = PhoneNumberValidator()
    
    phone_number = models.CharField(_("تلفن همراه"), max_length=20, validators=[phone_number_validator], unique=True)
    first_name = models.CharField(_("نام"), max_length=150, blank=True)
    is_active = models.BooleanField(_("فعال"), default=True)
    date_joined = models.DateTimeField(_("زمان ثبت نام"), default=timezone.now)
    password = models.CharField(_("password"), max_length=128, blank=True)
    username = models.CharField(_("username"), max_length=128, blank=True)
    
    EMAIL_FIELD = ""
    USERNAME_FIELD = "phone_number"
    objects = CustomUserManager()
    
    def __str__(self) -> str:
        return super().__str__()


class OTP(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="otps")
    otp_code = models.CharField(max_length=6)
    is_verified = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"OTP for {self.user.phone_number}"
