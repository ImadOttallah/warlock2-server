from django.db import models

class CastType(models.Model):
    name = models.CharField(max_length=50)
