from django.db import models
import datetime

# Create your models here.

class Signup(models.Model):
    username = models.CharField(max_length=250)
    email = models.EmailField()
    pwd = models.CharField(max_length=250)
    cnf_pwd = models.CharField(max_length=250)

    def __str__(self):
        return (self.username)
    
class Item(models.Model):
    i_type = models.CharField(max_length=250, null=True, blank=True)
    manufacturer = models.CharField(max_length=250, null=True, blank=True)
    v_type = models.CharField(max_length=250, null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    threshold = models.IntegerField(default = 10)

    def __str__(self):
        return (self.i_type + '-' + self.manufacturer + '-' + self.v_type)

class Sale(models.Model):
    i_type = models.CharField(max_length=250, null=True, blank=True)
    manufacturer = models.CharField(max_length=250, null=True, blank=True)
    v_type = models.CharField(max_length=250, null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True)
    items_sold = models.IntegerField(default = 0)
    cost = models.IntegerField(null=True, blank=True)
    sale_date = models.DateField(default=datetime.date.today)

    def __str__(self):
        return (self.i_type + '-' + self.manufacturer + '-' + self.v_type + '-' + str(self.quantity))