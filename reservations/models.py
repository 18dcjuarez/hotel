from django.db import models

from Room.models import Room
from Guest.models import Guest


class Reservation(models.Model):
    room = models.ForeignKey(Room, related_name='room_reservation', on_delete=models.PROTECT)
    guest = models.ForeignKey(Guest, related_name='guest_reservation', on_delete=models.PROTECT)
    start_date = models.DateField()
    end_date = models.DateField()
    deposit = models.IntegerField(null=False)
