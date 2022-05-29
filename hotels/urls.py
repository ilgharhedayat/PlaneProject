from django.urls import path
from .views import HotelView, HotelSearchView, HotelRoomsView

app_name = 'hotel'
urlpatterns = [
    path('', HotelView.as_view(), name='list'),
    path('search/', HotelSearchView.as_view(), name='search'),
    path('rooms/', HotelRoomsView.as_view(), name='rooms')
]
