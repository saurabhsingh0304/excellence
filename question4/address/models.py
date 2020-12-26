from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Customer(models.Model):
    user = models.OneToOneField(User, null=True,
                                on_delete=models.CASCADE)
    age = models.IntegerField(default=10)
    
    def __str__(self):
        return self.user.username


class Address(models.Model):
    Customer = models.ForeignKey(Customer, null=True,
                                 on_delete=models.CASCADE)
    street = models.CharField(max_length=50)
    pincode = models.IntegerField(default=000000)
    country = models.CharField(max_length=20)
    state = models.CharField(max_length=25)
    phone_num = models.IntegerField(default=9999999999)
