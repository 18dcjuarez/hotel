from rest_framework import viewsets
from rest_framework.response import Response

from .serializers import HotelSerializer, Hotel


class HotelViewSet(viewsets.ModelViewSet):
    serializer_class = HotelSerializer
    queryset = Hotel.objects.all()