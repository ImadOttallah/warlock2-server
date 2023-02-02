from django.db import models

class NpcType(models.Model):
    name = models.CharField(max_length=50)
