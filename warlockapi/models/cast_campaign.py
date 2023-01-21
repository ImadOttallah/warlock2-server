from django.db import models
from .cast import Cast
from .campaign import Campaign

class CastCampaign(models.Model):

    cast= models.ForeignKey(Cast, on_delete=models.CASCADE)
    campaign= models.ForeignKey(Campaign, on_delete=models.CASCADE)
