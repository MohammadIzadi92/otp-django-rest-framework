import re
from django.conf import settings
from django.core.mail import send_mail
from random import SystemRandom
from string import digits
from .settings import OTP_SETTINGS


def send_otp(otp):
    if (
        OTP_SETTINGS.SEND_OTP_TO_PHONE and
        otp.channel == "Phone" and
        OTP_SETTINGS.USER_PHONE_ATTR
    ):
        print(f"{otp.receiver}: {otp.password}")
    elif (
        OTP_SETTINGS.SEND_OTP_TO_EMAIL and
        otp.channel == "EMail" and
        OTP_SETTINGS.USER_EMAIL_ATTR
    ):
        send_mail(
            subject=OTP_SETTINGS.SUBJECT,
            message=OTP_SETTINGS.MESSAGE.format(otp.password),
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
