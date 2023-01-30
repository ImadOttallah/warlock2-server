from django.db import models
from .cast import Cast
from .campaign import Campaigns

class CastCampaign(models.Model):

    cast = models.ForeignKey(Cast, on_delete=models.CASCADE)
    campaign = models.ForeignKey(Campaigns, on_delete=models.CASCADE)
