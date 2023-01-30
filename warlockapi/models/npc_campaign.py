from django.db import models
from .npc import Npc
from .campaign import Campaigns

class NpcCampaign(models.Model):

    npc = models.ForeignKey(Npc, on_delete=models.CASCADE)
    campaign = models.ForeignKey(Campaigns, on_delete=models.CASCADE)
