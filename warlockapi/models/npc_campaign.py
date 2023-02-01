from django.db import models
# from .npc import Npc
# from .campaign import Campaign

class NpcCampaign(models.Model):

    npc = models.ForeignKey("Npc", on_delete=models.CASCADE)
    campaign = models.ForeignKey("Campaign", on_delete=models.CASCADE)
