from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import Hero_VillainSerializer
from .models import Hero_Villain
from heroes_villains import serializers

@api_view(['GET','POST'])
def heroes_villains_list(request):
    if request.method == 'GET':
        heroes_villains = Hero_Villain.objects.all()
        serializer = Hero_VillainSerializer(heroes_villains, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = Hero_VillainSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view (['GET', 'PUT'])
def hero_villain_detail(request, pk):
    hero_villain = get_object_or_404(Hero_Villain,pk=pk)
    if request.method == 'GET':
        serializer = Hero_VillainSerializer(hero_villain);
        return Response(serializer.data)
    elif request.method == 'PUT':
          serializer = Hero_VillainSerializer(Hero_Villain, data=request.data)
          serializer.is_valid(raise_exception=True)
          serializer.save()
          return Response(serializer.data)