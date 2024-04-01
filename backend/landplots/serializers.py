from rest_framework import serializers
from .models import LandPlot, ElectricityMeterIndicator

class LandPlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = LandPlot
        fields = '__all__'

class EMISerializer(serializers.ModelSerializer):
    class Meta:
        model = ElectricityMeterIndicator
        fields = '__all__'