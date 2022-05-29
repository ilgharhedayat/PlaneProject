from django.urls import path
from .views import ContactUsView, WorkWithView

app_name = 'core'
urlpatterns = [
    path('contact/', ContactUsView.as_view(), name='contact'),
    path('work/', WorkWithView.as_view(), name='work'),
]
