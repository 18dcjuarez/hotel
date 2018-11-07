from rest_framework import viewsets
from rest_framework.response import Response

from .serializers import ReservationSerializer, Reservation, \
                            ListReservationSerializer, CreateReservationSerializer, \
                            UpdateReservationSerializer


class ReservationViewSet(viewsets.ModelViewSet):
    serializer_class = ReservationSerializer
    queryset = Reservation.objects.all()

    def create(self, request):
        serializer = CreateReservationSerializer(data=request.data, context=request.data)
        print(serializer)
        serializer.is_valid(raise_exception=True)
        resp = serializer.crear()
        return Response(resp)

    # def list(self, request):
    #     data1 = request.query_params.dict()
    #     search = ListReservationSerializer(data=data1)
    #     search.is_valid(raise_exception=True)
    #     resp = search.listar()
    #     return Response(resp)

    def list(self, request):
        serializer = ListReservationSerializer()
        resp = serializer.show()
        # data1 = request.query_params.dict()
        # search = ListReservationSerializer(data=data1)
        # search.is_valid(raise_exception=True)
        # resp = search.listar()
        return Response(resp)

    def partial_update(self, request, pk=None):
        data = request.data
        data['id'] = pk
        serializer = UpdateReservationSerializer(data=data, context=data)
        serializer.is_valid(raise_exception=True)

        return Response('ok')
