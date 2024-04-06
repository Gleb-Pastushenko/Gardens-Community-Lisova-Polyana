from django.db import models
from django.contrib.auth.models import User

class LandPlot(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cadastral = models.DecimalField(max_digits=19, decimal_places=0)
    land_plot_number = models.CharField(max_length=200)
    well = models.BooleanField(default=False)
    electricity = models.BooleanField(default=False)
    fence = models.BooleanField(default=False)

class ElectricityMeterIndicator(models.Model):
    land_plot = models.ForeignKey(LandPlot, on_delete=models.CASCADE)
    emi_readings = models.DecimalField(max_digits=6, decimal_places=0)
    emi_serial = models.CharField(max_length=200)
    PHASE_CHOICES = [(1, '1 Фаза'), (3, '3 Фази')]
    emi_phases = models.IntegerField(choices=PHASE_CHOICES)