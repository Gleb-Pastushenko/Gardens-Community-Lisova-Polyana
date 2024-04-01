from rest_framework import serializers
from .models import Vacancy
from .models import Candidate

class VacancySerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        fields = ['id', 'text', 'title', 'expiration_date']
        
class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = ['id', 'name', 'vacancy']