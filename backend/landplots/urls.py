from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LandPlotViewSet, EMIViewSet

router = DefaultRouter()
router.register(r'landplots', LandPlotViewSet)
router.register(r'emi-s', EMIViewSet)

urlpatterns = [
    path('', include(router.urls)),
]