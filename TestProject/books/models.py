# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField('Author')
    publisher = models.ForeignKey('Publisher')
    publicathion_date = models.DateField()
    
    def __unicode__(self):  # __str__ on python 3
        return self.title
    
    
class Author(models.Model):
    salutation = models.CharField(max_length=100)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    
    def __unicode__(self):  # __str__ on python 3
        return self.name
    
class Publisher(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=50)
    website = models.URLField()
    
    def __unicode__(self):  # __str__ on python 3
        return self.name
    
    
class poster(models.Model):
    base_sige = models.IntegerField(max_length=10)
    coloer = models.CharField(max_length=100)
    