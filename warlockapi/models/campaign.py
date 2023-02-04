from django.db import models
from .user import User



class Campaign(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    npcs = models.ManyToManyField("Npc", through="NpcCampaign")
    casts = models.ManyToManyField("Cast", through="CastCampaign")
    name = models.CharField(max_length=50)
    image = models.CharField(max_length=300)
    description = models.CharField(max_length=300)
