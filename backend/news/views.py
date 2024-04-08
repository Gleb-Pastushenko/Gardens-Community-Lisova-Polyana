from rest_framework import viewsets
from django.db.models import Q
from .models import News
from .serializers import NewsSerializer

class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

    '''def get_queryset(self):
        query = self.request.query_params.get('q', None)
        if query is not None:
            return News.objects.filter(Q(title__icontains=query) | Q(text__icontains=query))
        return super().get_queryset()'''