from django.db import models

# Create your models here.

class Hero_Villian(models.Model):
    type = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    alter_ego = models.CharField(max_length=255)
    primary_ability = models.CharField(max_length=255)
    secondary_ability = models.CharField(max_length=255)
    catchphrase = models.CharField(max_length=255)