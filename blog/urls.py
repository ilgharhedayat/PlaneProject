from .views import ArticleListView, CategoryListView, ArticleDetailView
from django.urls import path

app_name = 'job'
urlpatterns = [
    path('', CategoryListView.as_view(), name='category'),
    path('article/<int:id>/', ArticleListView.as_view(), name='detail')
]
