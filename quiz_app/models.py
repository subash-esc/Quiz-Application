from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class Add_Quiz(models.Model):
    title = models.CharField(max_length=100,blank=True,null=True)
    thumbnail = models.ImageField(upload_to='thumbnail/')

    def __str__(self):
        return self.title 
