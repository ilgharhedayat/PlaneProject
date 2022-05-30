from .views import ArticleListView, CategoryListView, ArticleDetailView
from django.urls import path

app_name = 'blog'
urlpatterns = [
    path('', ArticleListView.as_view(), name='list'),
    path('category/', CategoryListView.as_view(), name='category'),
    path('article/<int:id>/', ArticleListView.as_view(), name='detail')
]
