from .views import JobListView, CategoryListView, JobDetailView
from django.urls import path

app_name = 'job'
urlpatterns = [
    path('', CategoryListView.as_view(), name='category'),
    path('job/<int:id>/', JobDetailView.as_view(), name='detail')
]
