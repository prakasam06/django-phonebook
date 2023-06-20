from django.db import models
from django.utils import timezone
from django.http import request
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.


class contacts(models.Model):
    
    name= models.CharField(max_length=300)
    phonenumber=models.IntegerField()
    email = models.EmailField()
    image = models.ImageField(blank=True,null=True,upload_to="images/")
    

