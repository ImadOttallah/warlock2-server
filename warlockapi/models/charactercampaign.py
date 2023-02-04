from django.db import models
# from .cast import Cast
# from .campaign import Campaign

class CharacterCampaign(models.Model):

    character = models.ForeignKey("Character", on_delete=models.CASCADE)
    campaign = models.ForeignKey("Campaign", on_delete=models.CASCADE)
