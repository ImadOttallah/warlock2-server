from django.db import models
from .user import User
from .castcategory import CastCategory

class Cast(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    castcategory = models.ForeignKey(CastCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    stamina = models.CharField(max_length=20)
    notes = models.CharField(max_length=300)
