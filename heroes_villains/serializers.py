from rest_framework import serializers
from .models import Hero_Villain

class Hero_VillainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hero_Villain
        fields = ['id','type','name','alter_ego','primary_ability','secondary_ability','secondary_ability','catchphrase','super_type', 'super_type_id']
        depth = 1

    super_type_id = serializers.IntegerField(write_only=True)