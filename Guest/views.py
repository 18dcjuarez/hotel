from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

from .serializers import GuestSerializer, Guest, \
                            CreateGuestSerializer, ListGuestSerializer, \
                            UpdateGuestSerializer, AddBalanceSerializer


class GuestViewSet(viewsets.ModelViewSet):
    serializer_class = GuestSerializer
    queryset = Guest.objects.all()

    def create(self, request):
        serializer = CreateGuestSerializer(data=request.data)
        resp = serializer.create()
        return Response(resp)
    
    def list(self, request):
        data = request.query_params.dict()
        serializer = ListGuestSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        resp = serializer.list()
        return Response(resp)
    
    def partial_update(self, request, pk=None):
        data = request.data
        data['id'] = pk
        guest = UpdateGuestSerializer(data=data)
        guest.is_valid(raise_exception=True)
        resp = guest.update()
        return Response(resp)
    
    def destroy(self, request, pk=None):
        return Response('Accion no permitida', status=400)
    
    @action(detail=True, methods=['PUT'])
    def add_balance(self, request, pk=None):
        print('estoy en add balance')
        print(request)
        data = request.data
        data['id'] = pk
        print(data)
        serializer = AddBalanceSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        return Response('ok')