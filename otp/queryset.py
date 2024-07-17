from django.db import models
from django.utils import timezone
from datetime import timedelta
from .settings import OTP_SETTINGS


class OTPCustomQuerySet(models.QuerySet):
    def is_valid(self, receiver, request_id, password):
        return self.filter(
            receiver=receiver,
            request_id=request_id,
            password=password,
            created__lt=timezone.now(),
            created__gt=timezone.now() - timedelta(seconds=OTP_SETTINGS.OTP_EXPIRATION_TIME_IN_SECOND)
        ).exists()
