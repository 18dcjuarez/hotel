from django.db import models


class Hotel(models.Model):
    name = models.CharField(null=False, max_length=50)
    address = models.CharField(null=False, max_length=70)
    rating = models.IntegerField(null=True)
    telephone = models.IntegerField(null=True)
