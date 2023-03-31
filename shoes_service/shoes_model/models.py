# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# This is our model for user registration.
class Shoes(models.Model):
    ### The following are the fields of our table.
    shoes_id = models.CharField(max_length=10)
    shoes_category = models.CharField(max_length=50)
    shoes_name = models.CharField(max_length=100)
    availability = models.CharField(max_length=15)
    price = models.CharField(max_length=10)
    ### It will help to print the values.
    def __str__(self):
        return '%s %s %s %s %s' % (self.shoes_id, self.shoes_category, self.shoes_name, self.availability, self.price)