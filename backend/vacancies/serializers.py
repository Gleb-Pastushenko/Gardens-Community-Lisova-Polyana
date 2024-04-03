from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Vacancy, Candidate

class VacancySerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        fields = ['id', 'text', 'title', 'expiration_date']

class CandidateSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    vacancy = serializers.PrimaryKeyRelatedField(queryset=Vacancy.objects.all())
    
    class Meta:
        model = Candidate
        fields = ['id', 'user', 'vacancy', 'price', 'votes']