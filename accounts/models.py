from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core.validators import RegexValidator
from django.db import models
from django_extensions.db.models import TimeStampedModel

from .managers import MyUserManager
from .uitils import get_file_path


# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=125, verbose_name="نام ")
    last_name = models.CharField(max_length=125, verbose_name="نام خانوادگی")
    user_name = models.CharField(max_length=125, unique=True, verbose_name="")
    email = models.EmailField(verbose_name="ایمیل")
    phone_number = models.CharField(
        max_length=11,
        verbose_name="شماره تلفن",
    )

    is_active = models.BooleanField(default=True, verbose_name="فعال")
    is_admin = models.BooleanField(default=False, verbose_name="ادمین")

    USERNAME_FIELD = "user_name"
    REQUIRED_FIELDS = ["first_name", "last_name", "email", "phone_number"]

    objects = MyUserManager()

    def __str__(self):
        return self.user_name

    @property
    def is_staff(self):
        return True

    class Meta:
        verbose_name = "کاربر"
        verbose_name_plural = "کاربران"


class OtpCode(models.Model):
    phone_number = models.CharField(max_length=11, verbose_name="شماره تماس")
    code = models.PositiveSmallIntegerField(verbose_name="کد ارسالی")
    created = models.DateTimeField(auto_now=True, verbose_name="تاریخ ارسال")

    def __str__(self):
        return f"{self.phone_number} - {self.code} - {self.created}"

    class Meta:
        verbose_name = "کد  ارسالی"
        verbose_name_plural = "کد های ارسالی"


class UserDocument(TimeStampedModel):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="document", verbose_name="کاربر"
    )
    national_card = models.ImageField(
        upload_to=get_file_path, verbose_name="تصویر کد ملی"
    )
    identity_card = models.ImageField(
        upload_to=get_file_path, verbose_name="تصویر شناسنامه"
    )
    passport = models.ImageField(
        upload_to=get_file_path, blank=True, verbose_name="تصویر پاسپورت"
    )
    other = models.ImageField(
        upload_to=get_file_path, blank=True, verbose_name="سایر مدارک"
    )
    bind = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user}  مدارک "

    class Meta:
        verbose_name = "مدرک"
        verbose_name_plural = "مدارک"
