from django.shortcuts import render
from rest_framework import viewsets,serializers
from rest_framework.response import Response
from .serializers import RoomSerializer,ListRoomSerializer, CreateRoomSerializer, UpdateSerializer
from .models import Room
# Create your views here.

class RoomViewSet(viewsets.ModelViewSet):

    def create(self, request):
        serializer = CreateRoomSerializer(data=request.data, context=request.data)
        print(serializer)
        serializer.is_valid(raise_exception=True)
        resp = serializer.crear()
        return Response(resp)

    def partial_update(self, request, pk=None):
        data1 = request.data
        data1['id'] = pk
        room = UpdateSerializer(data=data1)
        room.is_valid(raise_exception=True)
        response = room.update()
        return Response(response)

    def list(self, request):
        serializer = ListRoomSerializer()
        resp = serializer.show()
        return Response(resp)

