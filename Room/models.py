from django.db import models

from Hotel.models import Hotel


class Room(models.Model):
    number = models.IntegerField(null=False)
    floor = models.IntegerField(null=False)
    types = models.CharField(null=False, max_length=20)
    status = models.BooleanField(null=False, default= True)
    beds = models.IntegerField(null=False)
    max_capacity = models.IntegerField(null=False)
    day_cost = models.IntegerField(null=False)
    id_hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, null=True, default=None, related_name="hotel")





