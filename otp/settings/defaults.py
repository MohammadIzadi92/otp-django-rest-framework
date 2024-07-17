DEFAULT_OTP_SETTINGS = {
    "SEND_OTP_TO_EMAIL": False,
    "SEND_OTP_TO_PHONE": False,
    "USER_PHONE_ATTR": "username",
    "USER_EMAIL_ATTR": "username",
    "OTP_EXPIRATION_TIME_IN_SECOND": 120,
    "OTP_LENGTH": 6,
    "EMAIL_REGEX": r"(^[a-zA-Z0-9_.%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z0-9-.]{2,7}$)",
    "PHONE_REGEX": r"(^(?:\+?\d{1,2}\s?)?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}$)",
    "SUBJECT": "Verification OTP",
    "MESSAGE": "You should use this otp code to login : {}",
    "JWT_Authentication": False,
}
