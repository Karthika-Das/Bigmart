from django.db import models

# Create your models here.
class bigdb(models.Model):
    Cname=models.CharField(max_length=100,null=True,blank=True)
    Description=models.CharField(max_length=100,null=True,blank=True)
    Image=models.ImageField(upload_to="Image",null=True,blank=True)

class productdb(models.Model):
    Category=models.CharField(max_length=100,blank=True,null=True)
    Product=models.CharField(max_length=100,blank=True,null=True)
    Description=models.CharField(max_length=100,blank=True,null=True)
    Price=models.IntegerField(blank=True,null=True)
    Image=models.ImageField(upload_to="Image",blank=True,null=True)



