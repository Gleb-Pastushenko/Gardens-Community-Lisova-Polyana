from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AdvertisementViewSet, ImageViewSet

router = DefaultRouter()
router.register(r'', AdvertisementViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('<int:advertisement_id>/images/', ImageViewSet.as_view({'get': 'list'}))
]