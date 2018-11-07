from rest_framework import serializers

from .models import Reservation, Room, Guest
from Room.serializers import RoomInfoSerializer
from Guest.serializers import GuestSerializer

from datetime import date, datetime


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'


class ListReservationSerializer(serializers.Serializer):
    def listar(self):
        reservations = Reservation.objects.all()
        resp = ReservationSerializer(reservations, many=True).data
        return resp

    def show(self):
        reservations = Reservation.objects.all()
        return ReservationInfoSerializer(reservations, many=True).data


class CreateReservationSerializer(ReservationSerializer):
    room = serializers.IntegerField()
    guest = serializers.IntegerField()
    start_date = serializers.DateField()
    end_date = serializers.DateField()
    deposit = serializers.IntegerField()

    def validate_room(self, param):
        if Room.objects.filter(id=param):
            return param
        else:
            raise serializers.ValidationError('Room not exist')

    def validate_guest(self, param):
        if Guest.objects.filter(id=param):
            return param
        else:
            raise serializers.ValidationError('Guest not exist')

    def validate_start_date(self, param):
        if param > date.today():
            return param
        else:
            raise serializers.ValidationError('Invalid Date')

    def validate_end_date(self, param):
        a = datetime.strptime(self.context['start_date'], '%Y-%m-%d').date()
        if param > a:
            return param
        else:
            raise serializers.ValidationError('Invalid Date')

    def validate_deposit(self, param):
        if param > 0:
            return param
        else:
            raise serializers.ValidationError('Insufficient Deposit')

    def crear(self):
        reservation = Reservation()
        room = Room.objects.get(id=self.validated_data.get('room'))
        reservation.room = room
        guest = Guest.objects.get(id=self.validated_data.get('guest'))
        reservation.guest = guest
        reservation.start_date = self.validated_data.get('start_date')
        reservation.end_date = self.validated_data.get('end_date')
        reservation.deposit = self.validated_data.get('deposit')
        reservation.save()
        return ReservationSerializer(reservation).data


class ReservationInfoSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    start_date = serializers.DateField()
    end_date = serializers.DateField()
    deposit = serializers.IntegerField()
    room = RoomInfoSerializer()
    guest = GuestSerializer()


class UpdateReservationSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    start_date = serializers.DateField(required=False)
    end_date = serializers.DateField(required=False)
    deposit = serializers.IntegerField(required=False)
    room = serializers.IntegerField(required=False)
    guest = serializers.IntegerField(required=False)

    def validate_id(self, param):
        if Reservation.objects.filter(id=param):
            return param
        else:
            return serializers.ValidationError("Id no existe")

    def validate_deposit(self, param):
        if param >= 0:
            return param
        else:
            raise serializers.ValidationError("Deposito tiene que ser mayor a 0")

    def validate(self, param):
        reservation = Reservation.objects.get(pk=self.context.get('id'))
        new_start_date = self.initial_data.get('start_date',
                                               datetime.strftime(reservation.start_date, '%Y-%m-%d'))
        new_end_date = self.initial_data.get('end_date',
                                             datetime.strftime(reservation.end_date, '%Y-%m-%d'))
        deposit = self.initial_data.get('deposit', reservation.deposit)
        r1 = Room.objects.filter(id=self.context['id']).first()
        g1 = Guest.objects.filter(id=self.context['id']).first()
        if new_start_date and new_end_date:
            start_date = datetime.strptime(new_start_date, '%Y-%m-%d').date()
            end_date = datetime.strptime(new_end_date, '%Y-%m-%d').date()
            days = (end_date - start_date).days
            daily_cost = r1.day_cost
            balance = g1.balance
            total_cost = days * daily_cost
            total_balance = balance + deposit
            if start_date >= date.today():
                pass
            else:
                raise serializers.ValidationError("La Fecha de inicio tiene que ser mayor o igual a la de hoy")
            if end_date > start_date:
                pass
            else:
                raise serializers.ValidationError("La fecha de salida tiene que ser mayor o igual a la de inicio")
            if total_balance >= total_cost:
                total_balance -= total_cost
                pass
            else:
                raise serializers.ValidationError("Saldo insuficiente")
        return param
