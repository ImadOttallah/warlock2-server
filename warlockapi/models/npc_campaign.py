from django.db import models
from .npc import Npc
from .campaign import Campaign

class NpcCampaign(models.Model):

    npc_id= models.ForeignKey(Npc, on_delete=models.CASCADE)
    campaign_id= models.ForeignKey(Campaign, on_delete=models.CASCADE)
