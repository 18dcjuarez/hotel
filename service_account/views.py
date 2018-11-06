from rest_framework import viewsets
from .serializers import ServiceAccountSerializer, ServiceAccount


class ServiceAccountViewSet(viewsets.ModelViewSet):
    serializer_class = ServiceAccountSerializer
    queryset = ServiceAccount.objects.all()
