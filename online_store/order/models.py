from django.db import models


# Create your models here.

class Client(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(8)


class Item(models.Model):
    name = models.CharField(max_length=30)
    section = models.CharField(max_length=30)
    price = models.FloatField()


class Order(models.Model):
    number = models.IntegerField()
    date = models.DateField()
    is_delivered = models.BooleanField()
