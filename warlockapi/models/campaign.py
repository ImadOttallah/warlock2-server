from django.db import models
from django.utils import timezone, dateformat
from .user import User



class Campaign(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    npcs = models.ManyToManyField("Npc", through="NpcCampaign")
    casts = models.ManyToManyField("Cast", through="CastCampaign")
    name = models.CharField(max_length=50)
    image = models.CharField(max_length=300)
    date_created = models.DateTimeField(default=dateformat.format(timezone.now(), 'Y-m-d H:i:s'), null=True, blank=True)
    description = models.CharField(max_length=300)
