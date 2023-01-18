from django.db import models
from .user import User

class Campaign(models.Model):

    user_id= models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    image = models.CharField(max_length=300)
    date_created = models.DateField()
    description = models.CharField(max_length=300)
    
