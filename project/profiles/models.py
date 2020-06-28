from django.db import models

# Create your models here.

class UserForm(models.Model):
    title = models.TextField(max_length=30)
    description = models.TextField(max_length=30)
    feautured = models.BooleanField(default=True)