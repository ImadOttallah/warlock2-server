from django.db import models
# from .npc import Npc
from .npc_type import NpcType

class NpcCategory(models.Model):

    # npc = models.ForeignKey(Npc, on_delete=models.CASCADE)
    npc_type = models.ForeignKey(NpcType, on_delete=models.CASCADE)
