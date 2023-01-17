from django.db import models
from .cast import Cast
from .campaign import Campaign

class CastCampaign(models.Model):

    cast_id= models.ForeignKey(Cast, on_delete=models.CASCADE)
    campaign_id= models.ForeignKey(Campaign, on_delete=models.CASCADE)
