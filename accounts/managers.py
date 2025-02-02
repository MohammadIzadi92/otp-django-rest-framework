from django.contrib.auth.base_user import BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, phone_number="", first_name="", password="", **other_fields):
        user = self.model(phone_number=phone_number, first_name=first_name, **other_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, **other_fields):
        other_fields.setdefault("is_staff", True)
        other_fields.setdefault("is_superuser", True)
        other_fields.setdefault("is_active", True)
        if other_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff = True")
        if other_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser = True")
        return self.create_user(**other_fields)
