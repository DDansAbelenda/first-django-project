from django.db.models import *


# Create your models here.

class Client(Model):
    name = CharField(max_length=40)
    address = CharField(max_length=50)
    email = EmailField()
    phone = CharField(max_length=8)


class Item(Model):
    name = CharField(max_length=30)
    section = CharField(max_length=30)
    price = FloatField(verbose_name='value')

    def __str__(self):
        return self.name



class Order(Model):
    number = IntegerField()
    date = DateField()
    is_delivered = BooleanField()
