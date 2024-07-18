import re
from django.conf import settings
from django.core.mail import send_mail
from decouple import config
from kavenegar import (
    KavenegarAPI,
    APIException,
    HTTPException
)
from random import SystemRandom
from string import digits
from .settings import OTP_SETTINGS


def send_otp(otp):
    if (
        OTP_SETTINGS.SEND_OTP_TO_PHONE and
        otp.channel == "Phone" and
        OTP_SETTINGS.PHONE_NUMBER_STORAGE_FIELD_IN_THE_USER_MODEL
    ):
        try:
            api = KavenegarAPI(config("KAVENEGAR_KEY"))
            params = {
                'receptor': f"{otp.receiver}",
                'template': 'test',
                'token': f"{otp.password}",
                'type': 'sms',
            }   
            response = api.verify_lookup(params)
        except APIException as e: 
            pass
        except HTTPException as e: 
            pass
    elif (
        OTP_SETTINGS.SEND_OTP_TO_EMAIL and
        otp.channel == "EMail" and
        OTP_SETTINGS.EMAIL_STORAGE_FIELD_IN_THE_USER_MODEL
    ):
        send_mail(
            subject=OTP_SETTINGS.EMAIL_SUBJECT,
            message=OTP_SETTINGS.EMAIL_MESSAGE.format(otp.password),
            from_email=settings.EMAIL_HOST,
            recipient_list=[otp.receiver]
        )


def get_channel(receiver):
    if OTP_SETTINGS.SEND_OTP_TO_EMAIL:
        if re.fullmatch(OTP_SETTINGS.EMAIL_REGEX, receiver):
            return "EMail"
    if OTP_SETTINGS.SEND_OTP_TO_PHONE:
        if re.fullmatch(OTP_SETTINGS.PHONE_REGEX, receiver):
            return "Phone"
    return "Phone"


def generate_random_otp():
    rand = SystemRandom()
    otp_list = rand.choices(digits, k=OTP_SETTINGS.OTP_LENGTH)
    return "".join(otp_list)
