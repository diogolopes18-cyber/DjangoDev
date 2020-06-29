from django.db import models
import datetime as dt
# Create your models here.

class UserForm(models.Model):
    username = models.CharField(max_length=10)
    password = models.CharField(max_length=10)