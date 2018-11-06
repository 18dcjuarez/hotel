from django.db import models

from Guest.models import Guest


class Balance(models.Model):
    guest = models.ForeignKey(Guest, related_name='guest_balance', on_delete=models.CASCADE)
    amount = models.IntegerField(null=False)

