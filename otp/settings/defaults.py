DEFAULT_OTP_SETTINGS = {
    "SEND_OTP_TO_EMAIL": False,
    "SEND_OTP_TO_PHONE": False,
    "PHONE_NUMBER_STORAGE_FIELD_IN_THE_USER_MODEL": "username",
    "EMAIL_STORAGE_FIELD_IN_THE_USER_MODEL": "username",
    "OTP_EXPIRATION_TIME_IN_SECOND": 120,
    "OTP_LENGTH": 6,
    "EMAIL_REGEX": r"(^[a-zA-Z0-9_.%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z0-9-.]{2,7}$)",
    "PHONE_REGEX": r"(^(?:\+?\d{1,2}\s?)?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}$)",
    "EMAIL_SUBJECT": "Verification OTP",
    "EMAIL_MESSAGE": "You should use this otp code to login : {}",
    "JWT_Authentication": False,
}
