from django.conf import settings
from .defaults import DEFAULT_OTP_SETTINGS


class __DictClass:
    def __init__(self, _dict: dict) -> None:
        for key, value in _dict.items():
            setattr(self, key, value)


DEFAULT_OTP_SETTINGS.update(settings.OTP_SETTINGS)

OTP_SETTINGS = __DictClass(DEFAULT_OTP_SETTINGS)
