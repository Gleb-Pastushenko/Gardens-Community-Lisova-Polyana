from django.db import models
from accounts.models import User

class Vacancy(models.Model):
    text = models.TextField()
    title = models.CharField(max_length=200)
    expiration_date = models.DateField()

class Candidate(models.Model):
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    votes = models.IntegerField(default=0)