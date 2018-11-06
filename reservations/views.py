from rest_framework import viewsets
from .serializers import ReservationSerializer, Reservation


class ReservationViewSet(viewsets.ModelViewSet):
    serializer_class = ReservationSerializer
    queryset = Reservation.objects.all()
