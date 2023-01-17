from django.db import models
from .cast import Cast
from .cast_type import CastType

class CastCategory(models.Model):

    cast_id= models.ForeignKey(Cast, on_delete=models.CASCADE)
    cast_type_id= models.ForeignKey(CastType, on_delete=models.CASCADE)