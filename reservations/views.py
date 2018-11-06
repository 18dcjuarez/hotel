from rest_framework import viewsets
from .serializers import ReservationSerializer, Reservation, ListReservationSerializer, CreateReservationSerializer

class ReservationViewSet(viewsets.ModelViewSet):
    serializer_class = ReservationSerializer
    queryset = Reservation.objects.all()


    def create(self, request):
        serializer = CreateReservationSerializer(data=request.data, context=request.data)
        print(serializer)
        serializer.is_valid(raise_exception=True)
        resp = serializer.crear()
        return Response(resp)

    def list(self, request):
        data1 = request.query_params.dict()
        search = LisReservationSerializer(data=data1)
        search.is_valid(raise_exception=True)
        resp = search.listar()
        return Response(resp)
