from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import VacancyViewSet, CandidateViewSet

router = DefaultRouter()
router.register(r'', VacancyViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('<int:vacancy_id>/candidates/', CandidateViewSet.as_view({'get': 'list'})),
]