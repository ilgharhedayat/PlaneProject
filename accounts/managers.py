from django.contrib.auth.models import BaseUserManager


class MyUserManager(BaseUserManager):
    def create_user(
        self, first_name, last_name, user_name, email, phone_number, password
    ):
        if not first_name:
            raise ValueError("this field is required")
        if not last_name:
            raise ValueError("this field is required")
        if not user_name:
            raise ValueError("this field is required")
        if not email:
            raise ValueError("this field is required")
        if not phone_number:
            raise ValueError("this field is required")
        user = self.model(
            first_name=first_name,
            last_name=last_name,
            user_name=user_name,
            email=email,
            phone_number=phone_number,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(
        self, first_name, last_name, user_name, email, phone_number, password
    ):
        user = self.create_user(
            first_name, last_name, user_name, email, phone_number, password
        )
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
