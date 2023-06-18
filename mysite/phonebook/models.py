from django.db import models
from django.utils import timezone

from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.


class contacts(models.Model):

 
    name= models.CharField(max_length=300)
    phonenumber=models.IntegerField()
