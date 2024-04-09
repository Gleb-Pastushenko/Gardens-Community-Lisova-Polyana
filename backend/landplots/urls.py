from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LandPlotViewSet, EMIViewSet

router = DefaultRouter()
router.register(r'', LandPlotViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('<int:landplot_id>/emis/', EMIViewSet.as_view({'get': 'list'})),
]