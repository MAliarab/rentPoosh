from django.core.files.storage import FileSystemStorage
from django.db import models
from passlib.hash import pbkdf2_sha256

# Create your models here.
fs = FileSystemStorage(location="../static1/images")


class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=11)
    password = models.CharField(max_length=512)


class Address(models.Model):
    userID = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=250)


class Cloth(models.Model):
    name = models.CharField(max_length=100)
    size = models.IntegerField()
    color = models.CharField(max_length=50)
    price = models.FloatField()
    rentPrice = models.FloatField()
    brand = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    sex = models.CharField(max_length=20)
    category = models.CharField(max_length=100)
    occasion = models.CharField(max_length=30)
    rate = models.FloatField()
    stock = models.IntegerField()
    image = models.ImageField(upload_to="item_image", blank=True)

class Photo(models.Model):
    clothID = models.ForeignKey(Cloth, on_delete=models.CASCADE)
    photo = models.ImageField()


class Action(models.Model):
    userID = models.ForeignKey(User, on_delete=models.CASCADE)
    orderDate = models.DateField()
    saleID = models.CharField(max_length=250)
    clothID = models.ForeignKey(Cloth, on_delete=models.CASCADE)
    returnDate = models.DateField()
