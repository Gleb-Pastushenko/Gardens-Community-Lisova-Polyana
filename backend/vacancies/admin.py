from django.contrib import admin
from .models import Candidate, Vacancy

admin.site.register(Candidate)
admin.site.register(Vacancy)