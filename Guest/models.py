from django.db import models

from balance.models import Balance


class Guest(models.Model):
    name = models.CharField(null=False, max_length=20)
    address = models.CharField(null=False, max_length=30)
    balance = models.ForeignKey(Balance, related_name='guest_balance', on_delete=models.CASCADE)
    gender = models.CharField(null=False, max_length=10)
    dob = models.DateField(null=False)

