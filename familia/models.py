from pyexpat import model
from django.db import models


class Familiares(models.Model):

    objects = None
    name = models.CharField(max_length=30)
    age = models.PositiveIntegerField()
    date = models.DateField()
