from django.db import models

from reservations.models import Reservation
from Services.models import Services


class ServiceAccount(models.Model):
    reservation = models.ForeignKey(Reservation, related_name='reservation', on_delete=models.CASCADE)
    service = models.ForeignKey(Services, related_name='service', on_delete=models.CASCADE, default=None)
    quantity = models.IntegerField(null=False)
    cost = models.IntegerField(null=False)
    date = models.DateTimeField(auto_now_add=True)