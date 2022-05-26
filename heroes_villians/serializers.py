from rest_framework import serializers
from .models import Hero_Villian

class Hero_Villian(serializers,ModelSerializer):
    class Meta:
        model = Hero_Villian
        fields = ['type','name','alter_ago','primary_ability','secondary_ability','secondary_ability','catchphrase','super_type',]