from rest_framework import viewsets, response, status
from .models import Candidate, Vacancy
from .serializers import CandidateSerializer, VacancySerializer

class VacancyViewSet(viewsets.ModelViewSet):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer

class CandidateViewSet(viewsets.ModelViewSet):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer

    def perform_update(self, serializer):
        instance = self.get_object()
        instance.votes += 1
        instance.save()
        return response.Response(status=status.HTTP_204_NO_CONTENT)