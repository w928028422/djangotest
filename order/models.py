#coding=utf-8
from django.db import models
from django.contrib.auth.admin import User
# Create your models here.

class Product(models.Model):
    name = models.CharField('product name', max_length=30)
    price = models.FloatField('price', default=10)
    ptype = models.ForeignKey('Ptype')
    img = models.ImageField('img', upload_to='product', max_length=100)

    def __str__(self):
        return "%s ---> %f" % (self.name, self.price)

class Ptype(models.Model):
    name = models.CharField('type', max_length=10)

    def __str__(self):
        return "%s" % (self.name)

class Order(models.Model):
    orderDate = models.DateTimeField("order time", auto_now=True)
    product = models.ForeignKey('Product')
    user = models.ForeignKey('UserProfile')

class UserProfile(models.Model):
    SEX_CHOICES = (
        ('1','男'),
        ('2','女'),
    )
    username = models.OneToOneField(User)
    nickname = models.CharField('昵称',max_length=30)
    sex = models.CharField('性别',max_length=1,choices=SEX_CHOICES,default=1)
    address = models.CharField('地址',max_length=100,null=True)

