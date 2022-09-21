from statistics import mode
from django.db import models

# Create your models here.
class Service(models.Model):
    name = models.CharField(max_length=60)
    details = models.CharField(max_length=200)

# class 