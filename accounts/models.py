from django.db import models

from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True,blank=True)
    phone = models.BigIntegerField(null=True,blank=True)
    nationality = models.CharField(max_length=20,null=True)
