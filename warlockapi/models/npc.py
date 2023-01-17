from django.db import models
from .user import User

class Npc(models.Model):

    user_id= models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    image = models.CharField(max_length=300)
    actions = models.CharField(max_length=20)
    weapon = models.CharField(max_length=300)
    armour = models.CharField(max_length=20)
    adventuring_skills = models.CharField(max_length=20)
    stamina = models.CharField(max_length=20)
    notes = models.CharField(max_length=300)
    description = models.CharField(max_length=300)