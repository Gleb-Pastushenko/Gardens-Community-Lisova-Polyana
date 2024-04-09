from rest_framework import viewsets
from .models import LandPlot, ElectricityMeterIndicator
from .serializers import LandPlotSerializer, EMISerializer

class LandPlotViewSet(viewsets.ModelViewSet):
    queryset = LandPlot.objects.all()
    serializer_class = LandPlotSerializer

class EMIViewSet(viewsets.ModelViewSet):
    queryset = ElectricityMeterIndicator.objects.all()
    serializer_class = EMISerializer
    
    def get_queryset(self):
        landplot_id = self.kwargs.get('landplot_id')
        return ElectricityMeterIndicator.objects.filter(land_plot=landplot_id)