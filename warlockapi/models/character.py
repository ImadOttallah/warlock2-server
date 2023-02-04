from django.db import models
from .user import User

class Character(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=50)
    image = models.CharField(max_length=300)
    traits = models.CharField(max_length=300)
    notes = models.CharField(max_length=300)
    spells = models.CharField(max_length=300)
