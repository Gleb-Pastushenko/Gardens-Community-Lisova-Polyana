from rest_framework import generics, response, status
from .models import Candidate, Vacancy
from .serializers import CandidateSerializer, VacancySerializer

# відображення списку вакансій та створення нових вакансій
class ListCreateVacancy(generics.ListCreateAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer
    
# отримання, оновлення та видалення конкретної вакансії
class RetrieveUpdateDestroyVacancy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer
    
# відображення списку кандидатів та створення нових кандидатів
class ListCreateCandidate(generics.ListCreateAPIView):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer
    
# отримання, оновлення та видалення конкретного кандидата
class RetrieveUpdateDestroyCandidate(generics.RetrieveUpdateDestroyAPIView):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer

# голосування за конкретного кандидата
class VoteForCandidate(generics.UpdateAPIView):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer

    def update(self, request, *args, **kwargs):
        candidate = self.get_object()
        candidate.votes += 1
        candidate.save()
        return response.Response(status=status.HTTP_204_NO_CONTENT)