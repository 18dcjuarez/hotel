from rest_framework import viewsets
from rest_framework.response import Response

from .serializers import ServicesSerializer, Services


class ServicesViewSet(viewsets.ModelViewSet):
    serializer_class = ServicesSerializer
    queryset = Services.objects.all()