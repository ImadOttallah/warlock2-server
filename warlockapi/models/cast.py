from django.db import models
from .user import User

class Cast(models.Model):

    user_id= models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    type = models.CharField(max_length=30)
    weapon = models.CharField(max_length=20)
    actions = models.CharField(max_length=20)
    weapon = models.CharField(max_length=20)
    armour = models.CharField(max_length=20)
    adventuring_skills = models.CharField(max_length=20)
    stamina = models.CharField(max_length=20)
    notes = models.CharField(max_length=300)
    description = models.CharField(max_length=300)
