from django.db import models


class Balance(models.Model):
    amount = models.IntegerField(null=False)

