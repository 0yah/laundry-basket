#Use GIS models
from django.contrib.gis.db import models

#Extend the User Model 
from django.contrib.auth.models import AbstractUser, User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from .managers import UserManager

class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    USER_TYPE_CHOICES = (
      (1, 'Admin'),
      (2, 'Customer'),      
      (3, 'Rider'),
      (4, 'Staff'),
    )
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES,default=2)
    phone = models.CharField(max_length=30)
    
    objects = UserManager()

    def __str__(self):
        if self.first_name and self.last_name:
            return f'{self.first_name} {self.last_name}'

        return self.email 
# Create your models here.
class Rider(models.Model):
    RIDER_STATUS = [
        ("AV", "Available"),
        ("PC", "Picking"),
        ("DL", "Delivering"),
    ]
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    vehicle = models.CharField(max_length=30)
    status = models.CharField(choices=RIDER_STATUS,default="AV",max_length=30)

    
class Item(models.Model):
    price = models.IntegerField(default=0)
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name

class Mpesa(models.Model):
    reciept = models.CharField(max_length=50)
    date = models.DateTimeField()
    checkoutRequest = models.CharField(max_length=100) 
    amount = models.FloatField()

    def __str__(self) -> str:
        return f'{self.reciept} {self.amount}'

class Location(models.Model):
    
    pin = models.PointField(blank=True,null=True)
    floor = models.CharField(help_text="Floor Number",max_length=30,default="")
    street = models.CharField(help_text="Street Address",max_length=30,default="")
    apt = models.CharField(help_text="Apartment",max_length=30,default="")
    
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
    customer = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    status = models.CharField(choices=ORDER_STATUS,default="IN",max_length=30)
    pickedDay = models.DateTimeField(blank=True,null=True)
    deliveryDay = models.DateField(blank=True,null=True)
    price = models.FloatField(default=0.0)
    payment = models.ForeignKey("Mpesa",on_delete=models.CASCADE,blank=True,null=True)
    location = models.ForeignKey(Location,on_delete=models.CASCADE,blank=True,null=True)

    def __str__(self) -> str:
        return f'{self.customer.first_name} {self.customer.last_name}'
class OrderDetail(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE,blank=True,null=True)
    item = models.ForeignKey(Item,on_delete=models.CASCADE,blank=True,null=True)
    quantity = models.IntegerField(default=1)


