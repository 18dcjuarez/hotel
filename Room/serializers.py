from rest_framework import serializers
from .models import Room
from Hotel.models import Hotel
from Hotel.serializers import HotelSerializer


class RoomSerializer(serializers.ModelSerializer):

    class Meta:
        model = Room
        fields = '__all__'

class ListRoomSerializer(serializers.Serializer):

    def listar(self):
       rooms = Room.objects.all()
       resp = RoomSerializer(rooms, many=True).data
       return resp

    def show(self):
        room = Room.objects.all()
        return RoomInfoSerializer(room, many=True).data

class CreateRoomSerializer(RoomSerializer):

    number = serializers.IntegerField()
    id_hotel = serializers.IntegerField()

    def validate_number(self, param):
        print("validate number")
        print(self.context['id_hotel'])
        if len(Room.objects.filter(number=param, id_hotel=self.context['id_hotel'])) > 0:
            raise serializers.ValidationError("Room already exist")
        else:
            print("Created room")
            return param

    def validate_id_hotel(self, param):
        if Hotel.objects.filter(id=param):
            return param
        else:
            raise serializers.ValidationError('Hotel not exist')

    def crear(self):
        print("estoy en crear")
        print(self.validated_data)
        room = Room()
        room.number = self.validated_data.get('number')
        room.floor = self.validated_data.get('floor')
        room.types = self.validated_data.get('types')
        room.status = self.validated_data.get('status')
        room.beds = self.validated_data.get('beds')
        room.max_capacity = self.validated_data.get('max_capacity')
        room.day_cost = self.validated_data.get('day_cost')
        hotel = Hotel.objects.get(id=self.validated_data.get('id_hotel'))
        room.id_hotel = hotel
        room.save()
        return RoomSerializer(room).data


class UpdateSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    number = serializers.IntegerField(required=False)
    floor = serializers.IntegerField(required=False)
    types = serializers.CharField(required=False)
    status = serializers.BooleanField(required=False)
    beds = serializers.IntegerField(required=False)
    max_capacity = serializers.IntegerField(required=False)
    day_cost = serializers.IntegerField(required=False)

    def validate_id(self, param):
        if Room.objects.filter(id=param):
            return param
        else:
            raise serializers.ValidationError("Id no existe")

    def update(self):
        room = Room.objects.get(pk=self.validated_data.get('id'))
        room.number = self.validated_data.get('number', room.number)
        room.floor = self.validated_data.get('floor', room.floor)
        room.types = self.validated_data.get('types', room.types)
        room.status = self.validated_data.get('status', room.status)
        room.beds = self.validated_data.get('beds', room.beds)
        room.max_capacity = self.validated_data.get('max_capacity', room.max_capacity)
        room.day_cost = self.validated_data.get('day_cost', room.day_cost)
        room.save()
        return RoomSerializer(room).data


class RoomInfoSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    number = serializers.IntegerField()
    floor = serializers.IntegerField()
    types = serializers.CharField()
    status = serializers.BooleanField()
    beds = serializers.IntegerField()
    max_capacity = serializers.IntegerField()
    day_cost = serializers.IntegerField()
    id_hotel = HotelSerializer()
