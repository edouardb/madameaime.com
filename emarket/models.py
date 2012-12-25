from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from django.db import models

import stockmgmt


class Sale(models.Model):

    def __unicode__(self):
        return self.name

    name        = models.CharField(max_length=255)
    description = models.TextField(null=True, default=None, blank=True)
    begin       = models.DateTimeField(null=True, default=None, blank=True)
    end         = models.DateTimeField(null=True, default=None, blank=True)
    product     = models.ForeignKey(stockmgmt.models.Product)
    price       = models.DecimalField(max_digits=5, decimal_places=2)


class Order(models.Model):

    def __unicode__(self):
        return self.exposed_id

    exposed_id = models.CharField(max_length=32)
    date       = models.DateTimeField(auto_now_add=True)
    user       = models.ForeignKey(User)
    billing    = models.ForeignKey('Address')


class OrderSale(models.Model):

    def __unicode__(self):
        return self.order.exposed_id

    order    = models.ForeignKey(Order)
    sale     = models.ForeignKey(Sale)
    delivery = models.ForeignKey('Address', null=True, default=None, blank=True)


class Address(models.Model):

    def __unicode__(self):
        return u'%s %s' % (self.firstname, self.lastname)

    firstname   = models.CharField(max_length=64)
    lastname    = models.CharField(max_length=64)
    email       = models.EmailField()
    address     = models.TextField()
    additionnal = models.TextField(null=True, default=None, blank=True)
    zip_code    = models.CharField(max_length=16)
    city        = models.CharField(max_length=64)
    phone       = models.CharField(max_length=32, null=True, default=None, blank=True)
    country     = models.CharField(max_length=64)


class ShoppingCartLog(models.Model):
    sale    = models.ForeignKey(Sale)
    date    = models.DateTimeField(auto_now_add=True)
    session = models.ForeignKey(Session, null=True, default=None, blank=True)
    user    = models.ForeignKey(User)
