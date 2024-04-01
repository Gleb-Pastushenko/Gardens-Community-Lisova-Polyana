from django.db import models
from django.contrib.auth.models import User

def get_upload_to(instance, filename):
    return 'adv_pics/%s/%s' % (instance.advertisement.id, filename)

class Advertisement(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    title = models.CharField(max_length=200)

class Album(models.Model):
    advertisement = models.ForeignKey(Advertisement, related_name='adv_pics', on_delete=models.CASCADE)
    picture = models.ImageField(upload_to=get_upload_to)