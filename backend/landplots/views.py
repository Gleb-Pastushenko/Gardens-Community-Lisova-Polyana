from rest_framework import viewsets
from .models import LandPlot, ElectricityMeterIndicator
from .serializers import LandPlotSerializer, EMISerializer

class LandPlotViewSet(viewsets.ModelViewSet):
    queryset = LandPlot.objects.all()
    serializer_class = LandPlotSerializer

class EMIViewSet(viewsets.ModelViewSet):
    queryset = ElectricityMeterIndicator.objects.all()
    serializer_class = EMISerializer