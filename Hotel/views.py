from rest_framework import viewsets
from rest_framework.response import Response

from .serializers import HotelSerializer, Hotel


class HotelViewSet(viewsets.ModelViewSet):
    serializer_class = HotelSerializer
    queryset = Hotel.objects.all()

    def destroy(self, request, pk=None):
        return Response('Accion no permitida', status=400)
