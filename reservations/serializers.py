from rest_framework import serializers
from .models import Reservation, Room, Guest
from datetime import date,timedelta, datetime
from django.db.models import Q


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'


class ListReservationSerializer(serializers.Serializer):

    def listar(self):
        reservations = Reservation.objects.all()
        resp = ReservationSerializer(reservations, many=True).data
        return resp


class CreateReservationSerializer(ReservationSerializer):

    room = serializers.IntegerField()
    guest = serializers.IntegerField()
    start_date = serializers.DateField()
    end_date =serializers.DateField()
    deposit = serializers.IntegerField()

    def validate_room(self, param):
        if Room.objects.filter(id =param):
            return param
        else:
            raise serializers.ValidationError('Room not exist')

    def validate_guest(self,param):
        if Guest.objects.filter(id=param):
            return param
        else:
            raise serializers.ValidationError('Guest not exist')

    def validate_start_date(self, param):
        if param > date.today():
            print(date.today())
            return param
        else:
            raise serializers.ValidationError('Invalid Date')

    def validate_end_date(self, param):
        print(self.context)
        a=datetime.strptime(self.context['start_date'],'%Y-%m-%d').date()
        if param >= a:
            return param
        else:
            raise serializers.ValidationError('Invalid Date')

    def validate_deposit(self, param):
        if param > 0:
            return param
        else:
            raise serializers.ValidationError('Insufficient Deposit')

    def crear(self):
        print("estoy en crear")
        print(self.validated_data)
        reservation = Reservation()
        room = Room.objects.get(id = self.validated_data.get('room'))
        reservation.room = room
        guest = Guest.objects.get(id=self.validated_data.get('guest'))
        reservation.guest = guest
        reservation.start_date = self.validated_data.get('start_date')
        reservation.end_date = self.validated_data.get('end_date')
        id = self.validated_data.get('room')
        in_date = self.validated_data.get('start_date')
        end_date = self.validated_data.get('end_date')
        reservationLock= Reservation.objects.filter(Q(room = id) & (
                                      (Q(end_date__gte=in_date)&Q(end_date__lte=end_date))|
                                      (Q(start_date__lte=in_date)&Q(end_date__gte=end_date))|
                                      (Q(start_date__gt=in_date)&Q(start_date__lt=end_date))
                                      ))

        if reservationLock:
            return {'status:': 'reservaciones traslapadas', 'reservaciones': ReservationSerializer(reservationLock,
                                                                                                   many= True ).data}
        reservation.deposit = self.validated_data.get('deposit')
        reservation.save()
        return ReservationSerializer(reservation).data







