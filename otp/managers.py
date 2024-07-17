from django.db import models
from .extentions import get_channel
from .queryset import OTPCustomQuerySet


class OTPCustomManager(models.Manager):
    def get_queryset(self) -> models.QuerySet:
        return OTPCustomQuerySet(self.model, self._db)
    
    def is_valid(self, receiver, request_id, password):
        return self.get_queryset().is_valid(receiver, request_id, password)
    
    def generate(self, data):
        otp = self.model(
            receiver=data["receiver"],
            channel=get_channel(data["receiver"])
        )
        otp.save(using=self._db)
        return otp
