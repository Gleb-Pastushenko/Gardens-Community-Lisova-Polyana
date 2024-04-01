from django.urls import path
from .views import ListCreateVacancy, RetrieveUpdateDestroyVacancy, ListCreateCandidate, RetrieveUpdateDestroyCandidate, VoteForCandidate

urlpatterns = [
    path('vacancies/', ListCreateVacancy.as_view(), name='vacancy-list-create'),
    path('vacancies/<int:pk>/', RetrieveUpdateDestroyVacancy.as_view(), name='vacancy-detail'),
    path('candidates/', ListCreateCandidate.as_view(), name='candidate-list-create'),
    path('candidates/<int:pk>/', RetrieveUpdateDestroyCandidate.as_view(), name='candidate-detail'),
    path('candidates/<int:pk>/vote/', VoteForCandidate.as_view(), name='candidate-vote'),
]