from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import Hero_VillainSerializer
from .models import Hero_Villain

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
