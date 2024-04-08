from django.db import models

class News(models.Model):
    picture = models.ImageField(upload_to='news_pictures/')
    title = models.CharField(max_length=200, unique=True)
    text = models.TextField()

    def __str__(self):
        return self.title