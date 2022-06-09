from django.shortcuts import render
from rest_framework import permissions, viewsets
from .models import *
from .serializers import *
from rest_framework import viewsets
from django.db.models import Count
from rest_framework.response import Response
from rest_framework.decorators import action


class HouseViewSet(viewsets.ModelViewSet):
    queryset = House.objects.all()
    serializer_class = HouseSerializer

    def list(self, request, *args, **kwargs):
        if(request.GET.get('house_id')):
            house_id=request.GET.get('house_id')
            house=House.objects.get(id=house_id).rooms.all()
            serializedobj=RoomSerializer(house, many=True)
            return Response(serializedobj.data)
        else:
            return super().list(request, *args, **kwargs)   

    @action(detail=False)
    def room_count(self, request):
        house_id=request.GET.get('house_id', '')
        if house_id:
            q = House.objects.get(id=house_id).rooms.all()
            count = q.count()
            content = {'count': count}
            return Response(content)
        return Response('house_id Not found')
    
    @action(detail=False)
    def test(self, request):
        house_id=request.GET.get('house_id', '')
        while True:
            q = House.objects.get(id=house_id).rooms.all()
            count = q.count()
            content = {'count': count}
        return Response('house_id Not found')


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

    def list(self, request, *args, **kwargs):
        if(request.GET.get('room_type')):
            room_type=request.GET.get('room_type')
            r = self.queryset.filter(room_type=room_type)
            serializedobj=self.serializer_class(r, many=True)
            return Response(serializedobj.data)
        else:
            return super().list(request, *args, **kwargs)
