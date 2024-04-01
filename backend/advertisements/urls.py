from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AdvertisementViewSet, AlbumViewSet

router = DefaultRouter()
router.register(r'advertisements', AdvertisementViewSet)
router.register(r'albums', AlbumViewSet)

urlpatterns = [
    path('', include(router.urls)),
]