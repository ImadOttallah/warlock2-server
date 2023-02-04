from django.db import models

class User(models.Model):
    uid = models.CharField(max_length=25)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    bio = models.CharField(max_length=100)
    profile_image_url = models.CharField(max_length=500)
    email = models.EmailField(max_length=25)
    created_on = models.DateField()
    active = models.BooleanField(default=False)
    