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

        super_type_param = request.query_params.get("super_type")
        supers = Hero_Villain.objects.all()
        serializer = Hero_VillainSerializer(supers, many=True)
        custom_response={}
        
        if super_type_param == 'Hero':
            supers =Hero_Villain.objects.filter(super_type_id = 1)
            serializer = Hero_VillainSerializer(supers, many=True)
            custom_response['Heroes'] = [
               serializer.data 
            ]
            return Response(custom_response)

        elif super_type_param == 'Villain':
            supers = Hero_Villain.objects.filter(super_type_id= 2)
            serializer = Hero_VillainSerializer(supers, many=True)
            custom_response['Villains'] = [
                serializer.data
            ]
            return Response(custom_response)

        heroes_villains = Hero_Villain.objects.all()
        serializer = Hero_VillainSerializer(heroes_villains, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = Hero_VillainSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view (['GET', 'PUT', 'DELETE'])
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
    elif request.method == 'DELETE':
        hero_villain.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)