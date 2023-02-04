from django.db import models
from .casttype import CastType
# from .cast import Cast

class CastCategory(models.Model):
    # cast = models.ForeignKey(Cast, on_delete=models.CASCADE)
    casttype = models.ForeignKey(CastType, on_delete=models.CASCADE)
