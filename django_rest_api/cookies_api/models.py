from django.db import models

# Create your models here.
class Cookie(models.Model):
    type = models.CharField(max_length=32)
    cost = models.FloatField()
    cost_to_make = models.FloatField()
    quantity = models.IntegerField()
    img = models.TextField()
    manufacturer = models.CharField(max_length=32)