# Login and Register via OTP

Login and register via otp for Django Rest Framework by phone number and email.

## Adjustment steps

### 1 - Add the app to the installed apps in project settings

```python
INSTALLED_APPS = [
    ...
    "otp.apps.OtpConfig",
    ...
]
```

### 2 - If you intend to use jwt, install it

```bash
pip install djangorestframework-simplejwt==5.3.1
```

### 3 - Put app settings in project settings

```python
OTP_SETTINGS = {
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
```

### 4 - Put email settings in the project settings

If you want to send the otp code to users via email, add email settings to Django settings

```python
# email fake
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# or

# send gmail
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = "EMAIL_HOST"
EMAIL_USE_TLS = True
EMAIL_PORT = "EMAIL_PORT"
EMAIL_HOST_USER = "EMAIL_HOST_USER"
EMAIL_HOST_PASSWORD = "EMAIL_HOST_PASSWORD"
```

### 5 - Rewriting the otp send function

If you want to send the otp code to the users via message, rewrite the following function

```python
# otp/extensions.py
def send_otp(otp):
    if (
        OTP_SETTINGS.SEND_OTP_TO_PHONE and
        otp.channel == "Phone" and
        OTP_SETTINGS.USER_PHONE_ATTR
    ):
        pass
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
```

### 6 - Eventually

```bash
python manage.py makemigrations
```

```bash
python manage.py migrate
```
