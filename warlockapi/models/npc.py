from django.db import models
from .user import User
from .npccategory import NpcCategory

class Npc(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    npccategory = models.ForeignKey(NpcCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    stamina = models.CharField(max_length=20)
    notes = models.CharField(max_length=300)
