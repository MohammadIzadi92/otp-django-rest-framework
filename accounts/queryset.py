from django.db import models
from django.utils import timezone
from datetime import timedelta


class OTPCustomQuerySet(models.QuerySet):
    def is_valid(self, receiver, request_id, password):
        return self.filter(
            receiver=receiver,
            request_id=request_id,
            password=password,
            created__lt=timezone.now(),
            created__gt=timezone.now() - timedelta(seconds=120)
        ).exists()
