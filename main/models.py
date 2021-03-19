#Use GIS models
from django.contrib.gis.db import models

#Extend the User Model 
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Rider(models.Model):
    RIDER_STATUS = [
        ("AV", "Available"),
        ("PC", "Picking"),
        ("DL", "Delivering"),
    ]
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    active = models.BooleanField(default=False)
    vehicle = models.CharField(max_length=30)
    status = models.CharField(choices=RIDER_STATUS,default="AV")
    phone = models.CharField()


class Customer(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    phone = models.CharField()

class Item(models.Model):
    price = models.IntegerField(default=0)
    name = models.CharField(max_length=25)

class Mpesa(models.Model):
    reciept = models.CharField(max_length=50)
    date = models.DateTimeField()
    checkoutRequest = models.CharField(max_length=100) 
    amount = models.FloatField()

class Location(models.Model):
    
    pin = models.PointField(blank=True,null=True)
    #Must be filled if point is NULL || Blank
    floor = models.CharField(blank=True,help_text="Floor Number")
    street = models.CharField(blank=True,null=True,help_text="Street Address")
    apt = models.CharField(blank=True,null=True,help_text="Apartment")
    
class Order(models.Model):
    ORDER_STATUS = [
        ("IN", "Initialised"),
        ("PY", "Paid"),
        ("TB", "To be picked"),
        ("PC", "Picked"),
        ("RC", "Received"),
        ("RE", "Ready"),
        ("TD", "To be delivered"),
        ("CM", "Completed"),
    ]
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    status = models.CharField(choices=ORDER_STATUS,default="IN")
    pickedDay = models.DateTimeField()
    deliveryDay = models.DateField()
    price = models.FloatField()
    payment = models.ForeignKey(Mpesa,on_delete=models.CASCADE)
    location = models.ForeignKey(Location)

class OrderDetail(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    item = models.ForeignKey(Item,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)


