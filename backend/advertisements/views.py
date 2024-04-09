from rest_framework import viewsets
from .models import Advertisement, Image
from .serializers import AdvertisementSerializer, ImageSerializer

class AdvertisementViewSet(viewsets.ModelViewSet):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer

class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

    def get_queryset(self):
        advertisement_id = self.kwargs.get('advertisement_id')
        return Image.objects.filter(advertisement=advertisement_id)