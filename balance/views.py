from rest_framework import viewsets

from .serializers import BalanceSerializer, Balance


class BalanceViewSet(viewsets.ModelViewSet):
    serializer_class = BalanceSerializer
    queryset = Balance.objects.all()
