from rest_framework import serializers
from .models import Advertisement, Album

class AdvertisementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertisement
        fields = ['user', 'text', 'title']

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ['advertisement', 'picture']