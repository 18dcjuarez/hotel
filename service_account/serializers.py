from rest_framework import serializers
from .models import ServiceAccount


class ServiceAccountSerializer(serializers.Serializer):
    class Meta:
        model = ServiceAccount
        fields = '__all__'
