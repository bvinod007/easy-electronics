from django.db import models

# Create your models here.
class Authentication(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    createdAt = models.DateTimeField(auto_now=True)

# class Products(models.Model):
#     productid = models.IntegerField(max_length=5, primary_key=True)
#     productname = models.CharField(max_length=50)
#     productmodel = models.CharField(max_length=50)
#     price = models.IntegerField(max_length=10)
#     rating = models.IntegerField(max_length=5)
