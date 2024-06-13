from django.db import models

# Create your models here.
class conytactdb(models.Model):
    Name=models.CharField(max_length=100,null=True,blank=True)
    Email=models.EmailField(max_length=100,null=True,blank=True)
    Phone=models.IntegerField(null=True,blank=True)
    Subject=models.CharField(max_length=100,null=True,blank=True)
    Messege=models.TextField(max_length=100,null=True,blank=True)

class registerdb(models.Model):
    Username=models.CharField(max_length=100,null=True,blank=True)
    Email=models.EmailField(max_length=100,null=True,blank=True)
    Password=models.EmailField(max_length=100,null=True,blank=True)

class cartdb(models.Model):
    Username=models.CharField(max_length=100,null=True,blank=True)
    Product_Name=models.CharField(max_length=100,null=True,blank=True)
    Quantity=models.IntegerField(null=True,blank=True)
    Total_price=models.IntegerField(null=True,blank=True)

class paymentdb(models.Model):
    Name=models.CharField(max_length=100,blank=True,null=True)
    Email=models.EmailField(max_length=100,blank=True,null=True)
    Address=models.TextField(max_length=100,blank=True,null=True)
    Phone=models.IntegerField(blank=True,null=True)
    Say=models.TextField(max_length=100,blank=True,null=True)
    Total_price=models.IntegerField(blank=True,null=True)



