from django.db import models
from django_extensions.db.models import TimeStampedModel
from django.conf import settings

user = settings.AUTH_USER_MODEL


# Create your models here.
class ReserveHotel(TimeStampedModel):
    user = models.ForeignKey(user, on_delete=models.CASCADE, related_name='reserved_hotel')
    check_in_time = models.TimeField()
    check_out_time = models.TimeField()
    check_in_date = models.DateField()
    check_out_date = models.DateField()

