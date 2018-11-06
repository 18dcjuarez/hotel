from rest_framework import serializers

from .models import Hotel


class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = '__all__'


class ListHotelSerializer(serializers.Serializer):

    def listar(self):
        rooms = Hotel.objects.all()
        resp = HotelSerializer(rooms, many=True).data
        return resp


class CreateHotelSerializer(HotelSerializer):

    name = serializers.CharField()

    def validate_name(self, param):
        if len(Hotel.objects.filter(name=param)) > 0:
            raise serializers.ValidationError("Hotel already exist")
        else:
            print("Created Hotel")
            return param

    def crear(self):
        hotel = Hotel()
        hotel.name = self.validated_data.get('name')
        hotel.address = self.validated_data.get('address')
        hotel.rating = self.validated_data.get('rating')
        hotel.telephone = self.validated_data.get('telephone')
        hotel.save()
        return HotelSerializer(hotel).data

class UpdateSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(required=False)
    address = serializers.CharField(required=False)
    rating = serializers.IntegerField(required=False)
    telephone = serializers.IntegerField(required=False)

    def validate_id(self, param):
        if Hotel.objects.filter(id=param):
            return param
        else:
            raise serializers.ValidationError("Id no existe")

    def update(self):
        hotel = Hotel.objects.get(pk=self.validated_data.get('id'))
        hotel.name = self.validated_data.get('name', hotel.name)
        hotel.address = self.validated_data.get('address', hotel.address)
        hotel.rating = self.validated_data.get('rating', hotel.rating)
        hotel.save()
        return HotelSerializer(hotel).data


