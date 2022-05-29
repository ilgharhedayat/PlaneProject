from django.contrib import admin

from .models import Passenger, Reservation

# Register your models here.


class PassengerInline(admin.StackedInline):
    model = Passenger
    extra = 1
    max_num = 1


class ReservationAdmin(admin.ModelAdmin):
    inlines = [
        PassengerInline,
    ]


admin.site.register(Passenger)
admin.site.register(Reservation, ReservationAdmin)
