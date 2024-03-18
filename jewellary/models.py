from django.db import models

# Create your models here.
class customer(models.Model):
    name = models.CharField(max_length=200,null=True)
    age = models.IntegerField()
    gender = models.CharField(max_length=200,null=True)
    email = models.CharField(max_length=200,null=True)
    phonenumber = models.IntegerField()
    username = models.CharField(max_length=200,null=True)
    password = models.CharField(max_length=200,null=True)

 


  

class staff(models.Model):
    name = models.CharField(max_length=200,null=True)
    age = models.IntegerField()
    gender = models.CharField(max_length=200,null=True)
    email = models.CharField(max_length=200,null=True)
    phonenumber = models.IntegerField()
    username = models.CharField(max_length=200,null=True)
    password = models.CharField(max_length=200,null=True)
    approval = models.BooleanField(default=False,null=True)

class products(models.Model):
    product_name = models.CharField(max_length=50)
    price = models.IntegerField()
    material = models.CharField(max_length=20)
    category = models.CharField(max_length=20)
    image = models.ImageField(upload_to='images/')
    def __str__(self):
        return self.product_name