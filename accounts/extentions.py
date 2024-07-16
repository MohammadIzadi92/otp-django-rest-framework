import re
# import kavenegar as kn
from decouple import config
from random import SystemRandom
from string import digits


def send_otp(otp):
    print(f"{otp.receiver}: {otp.password}")
    # try:
        # api = kn.KavenegarAPI(apikey=config("KAVENEGAR_TOKEN"))
        # params = {
            # "receptor": phone_number,
            # "token": otp,
            # "template": "Book Store"
        # }
        # api.verify_lookup(params=params)
    # except: pass


def get_channel(receiver):
    # phone_regex = r"(^(?:\+?\d{1,2}\s?)?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}$)"
    email_regex = r"(^[a-zA-Z0-9_.%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z0-9-.]{2,7}$)"
    if re.fullmatch(email_regex, receiver):
        return "E-Mail"
    return "Phone"


def generate_random_otp():
    rand = SystemRandom()
    otp_list = rand.choices(digits, k=6)
    return "".join(otp_list)
