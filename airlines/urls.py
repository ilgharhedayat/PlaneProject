from django.urls import path

from .views import SearchListView

app_name = "airlines"
urlpatterns = [
    path("fly_search/", SearchListView.as_view(), name="fly_search"),
]
