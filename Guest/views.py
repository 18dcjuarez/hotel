from rest_framework import viewsets
from rest_framework.response import Response

from .serializers import GuestSerializer, Guest

class GuestViewSet(viewsets.ModelViewSet):
    serializer_class = GuestSerializer
    queryset = Guest.objects.all()
