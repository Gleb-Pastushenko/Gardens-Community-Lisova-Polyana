from rest_framework import generics
from django.db.models import Q
from .models import News
from .serializers import NewsSerializer

# відображення списку всіх новин та створення нової новини
class ListCreateNews(generics.ListCreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

# відображення деталей конкретної новини, її редагування та видалення
class RetrieveUpdateDestroyNews(generics.RetrieveUpdateDestroyAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

# пошук новин за ключовими словами
class SearchNews(generics.ListAPIView):
    serializer_class = NewsSerializer

    def get_queryset(self):
        query = self.request.query_params.get('q', None)
        if query is not None:
            return News.objects.filter(Q(title__icontains=query) | Q(text__icontains=query))
        return News.objects.none()