from django.db import models

# Create your models here.

class Users(models.Model):
    fullname = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    email = models.CharField(max_length=30)
    username = models.CharField(max_length=10)
    password = models.EmailField(max_length=14)
    phone_number = models.CharField(max_length=10)


class Rol(models.Model):
    rol_name = models.CharField(max_length=10)

class Site(models.Model):
    site_name = models.CharField(max_length=10)