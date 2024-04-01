from django.urls import path
from .views import ListCreateNews, RetrieveUpdateDestroyNews, SearchNews

urlpatterns = [
    path('news/', ListCreateNews.as_view(), name='news-list-create'),
    path('news/<int:pk>/', RetrieveUpdateDestroyNews.as_view(), name='news-detail'),
    path('news/search/', SearchNews.as_view(), name='news-search'),
]