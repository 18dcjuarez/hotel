from rest_framework import serializers

from .models import Guest


class GuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guest
        fields = '__all__'


class CreateGuestSerializer(GuestSerializer):

    def create(self):
        guest = Guest()
        guest.name = self.initial_data.get('name')
        guest.address = self.initial_data.get('address')
        guest.balance = self.initial_data.get('balance')
        guest.gender = self.initial_data.get('gender')
        guest.dob = self.initial_data.get('dob')
        guest.save()
        return GuestSerializer(guest).data


class ListGuestSerializer(serializers.Serializer):

    def list(self):
        guest = Guest.objects.all()
        resp = GuestSerializer(guest, many=True).data
        return resp


class UpdateGuestSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(required=False)
    address = serializers.CharField(required=False)
    # balance = serializers.IntegerField(required=False)
    gender = serializers.CharField(required=False)
    dob = serializers.DateField(required=False)

    def validate_id(self, param):
        if Guest.objects.filter(id=param):
            return param
        else:
            return serializers.ValidationError("Id no existe")

    def update(self):
        guest = Guest.objects.get(pk=self.validated_data.get('id'))
        guest.name = self.validated_data.get('name', guest.name)
        guest.address = self.validated_data.get('address', guest.address)
        guest.balance = self.validated_data.get('balance', guest.balance)
        guest.gender = self.validated_data.get('gender', guest.gender)
        guest.dob = self.validated_data.get('dob', guest.dob)
        guest.save()
        return GuestSerializer(guest).data


class AddBalanceSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    balance = serializers.IntegerField()

    def validate_id(self, param):
        if Guest.objects.filter(id=param):
            return param
        else:
            return serializers.ValidationError("Id no existe")

    def add(self):
        add_balance = self.initial_data.get('balance')
        guest = Guest.objects.get(pk=self.validated_data.get('id'))
        # print("Se va a agregar: ", add_balance)
        # print("Saldo inicial: ", guest.balance)
        guest.balance += add_balance
        # print("Saldo Final: ", guest.balance)
        guest.save()
        return GuestSerializer(guest).data
