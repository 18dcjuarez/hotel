from rest_framework import viewsets
from rest_framework.response import Response

from .serializers import CreateHotelSerializer, HotelSerializer, Hotel, ListHotelSerializer, UpdateSerializer


class HotelViewSet(viewsets.ModelViewSet):
    serializer_class = HotelSerializer
    queryset = Hotel.objects.all()

    def destroy(self, request, pk=None):
        return Response('Accion no permitida', status=400)

    def create(self, request):
        serializer = CreateHotelSerializer(data=request.data)
        print(serializer)
        serializer.is_valid(raise_exception=True)
        resp = serializer.crear()
        return Response(resp)

    def list(self, request):
        data1 = request.query_params.dict()
        search = ListHotelSerializer(data=data1)
        search.is_valid(raise_exception=True)
        resp = search.listar()
        return Response(resp)

    def partial_update(self, request, pk=None):
        data1 = request.data
        data1['id'] = pk
        hotel = UpdateSerializer(data=data1)
        hotel.is_valid(raise_exception=True)
        response = hotel.update()
        return Response(response)

