from django.conf import settings
from django.db import models
from django.db.models import Sum
from django_extensions.db.models import TimeStampedModel
from airlines.models import Airline

user = settings.AUTH_USER_MODEL


# Create your models here.


class Reservation(models.Model):
    user = models.ForeignKey(
        user, on_delete=models.CASCADE, related_name="reservation", verbose_name="کاربر"
    )
    air_line = models.ForeignKey(Airline, on_delete=models.CASCADE, related_name='air_line_reservation', blank=True,
                                 null=True)
    fly_code = models.CharField(max_length=125, verbose_name="کد پرواز")
    flight_class = models.CharField(max_length=125, blank=True)
    flight_no = models.CharField(max_length=125, blank=True)
    source = models.CharField(max_length=125, verbose_name="مبذا")
    target = models.CharField(max_length=125, verbose_name="مقصد")
    # price = models.IntegerField(verbose_name='')
    date = models.CharField(max_length=125, verbose_name="تاریخ")
    email = models.EmailField()
    phone_number = models.CharField(max_length=125, verbose_name="شماره تماس")
    paid = models.BooleanField(default=False, verbose_name="پرداخت شده؟")
    pnr_code = models.CharField(max_length=125, blank=True, verbose_name='شناسه رزرو')

    def __str__(self):
        return f'{self.user}  رزروهای '

    def get_total_cost(self):
        return self.passengers.aggregate(Sum("price"))['price__sum']

    class Meta:
        verbose_name = "رزرو"
        verbose_name_plural = "رزروها"


class Passenger(models.Model):
    GENDER = (
        ("مرد", "مرد"),
        ("زن", "زن"),
    )
    en_name = models.CharField(
        max_length=125,
    )
    en_family = models.CharField(max_length=125, verbose_name="نام لایتن")
    gender = models.CharField(max_length=12, choices=GENDER, verbose_name="جنسیت")
    national_code = models.CharField(max_length=10, verbose_name="کد ملی")
    ir_name = models.CharField(max_length=125, verbose_name="نام")
    ir_family = models.CharField(max_length=125, verbose_name="نام خانوادگی")
    day = models.PositiveSmallIntegerField(verbose_name="ماه")
    month = models.CharField(max_length=25, verbose_name="سال")
    year = models.PositiveSmallIntegerField(verbose_name="روز")
    reserve = models.ForeignKey(
        Reservation,
        on_delete=models.CASCADE,
        related_name="passengers",
        verbose_name="رزرو کننده",
    )
    price = models.IntegerField(verbose_name="قیمت")
    age = models.CharField(max_length=125, verbose_name="سن")

    def __str__(self):
        return f"{self.ir_name} {self.ir_family}"

    def en_full_name(self):
        return f"{self.en_name} {self.en_family}"

    class Meta:
        verbose_name = "مسافر"
        verbose_name_plural = "مسافر ها"
