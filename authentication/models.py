from django.db import models

# Create your models here.
class Authentication(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    createdAt = models.DateTimeField(auto_now=True)
