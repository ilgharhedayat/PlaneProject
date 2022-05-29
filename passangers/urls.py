from django.urls import path

from .views import PassengerView, TripInfoView, go_to_gateway_view, cities, home, CancelTicketView

app_name = "passengers"
urlpatterns = [
    path("", home, name="home"),
    path('cancel/ticket/<int:reserve_id>/', CancelTicketView.as_view(), name='cancel_reserve'),
    path("trip/", TripInfoView.as_view(), name="trip"),
    # path("", go_to_gateway_view, name="pay"),
    path("toBank/", go_to_gateway_view, name="pay"),
    path("cities/", cities, name="cities"),
    path("passenger/", PassengerView.as_view(), name="passenger"),
]
