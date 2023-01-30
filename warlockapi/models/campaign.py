from django.db import models
from .user import User
from .character import Character
from .npc import Npc
from .cast import Cast

class Campaign(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    npc = models.ForeignKey(Npc, on_delete=models.CASCADE)
    cast = models.ForeignKey(Cast, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    image = models.CharField(max_length=300)
    date_created = models.DateField()
    description = models.CharField(max_length=300)
    
@property
def joined(self):
    return self.__joined

@joined.setter
def joined(self, value):
    self.__joined = value
