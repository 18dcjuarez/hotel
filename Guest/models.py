from django.db import models


class Guest(models.Model):
    name = models.CharField(null=False, max_length=20)
    address = models.CharField(null=False, max_length=30)
    balance = models.IntegerField(null=True, default=0)
    gender = models.CharField(null=False, max_length=10)
    dob = models.DateField(null=False)
