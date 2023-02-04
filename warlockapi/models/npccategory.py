from django.db import models
# from .npc import Npc
from .npctype import NpcType

class NpcCategory(models.Model):

    # npc = models.ForeignKey(Npc, on_delete=models.CASCADE)
    npctype = models.ForeignKey(NpcType, on_delete=models.CASCADE)
