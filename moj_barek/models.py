from django.db import models


# Create your models here.
class Butelka(models.Model):
    name = models.CharField(max_length=100)
    volume = models.DecimalField(max_digits=6, decimal_places=2)
    bougth = models.DateField()
