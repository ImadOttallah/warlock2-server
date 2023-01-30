from django.db import models
from .cast_type import CastType
from .cast import Cast

class CastCategory(models.Model):
    cast = models.ForeignKey(Cast, on_delete=models.CASCADE)
    cast_type = models.ForeignKey(CastType, on_delete=models.CASCADE)
