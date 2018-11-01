from django.db import models


class Services(models.Model):
    name = models.IntegerField(null=False)
    cost = models.FloatField(null=False)
    status = models.BooleanField(default=False)