from uuid import uuid4
from django.db import models
from .settings import OTP_SETTINGS
from .extentions import generate_random_otp
from .managers import OTPCustomManager


class OTPRequest(models.Model):    
    class OTPChannelChoices(models.TextChoices):
        PHONE = "Phone"
        EMAIL = "EMail"
    
    request_id = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    channel = models.CharField(max_length=10, choices=OTPChannelChoices.choices, default=OTPChannelChoices.PHONE)
    receiver = models.CharField(max_length=150)
    password = models.CharField(max_length=OTP_SETTINGS.OTP_LENGTH, default=generate_random_otp)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    
    objects = OTPCustomManager()
    
    def __str__(self):
        return f"OTP for {self.receiver}"
