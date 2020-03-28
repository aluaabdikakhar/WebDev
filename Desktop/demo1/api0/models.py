from django.db import models

class Product(models.Model):
    name = models.CharField(max_length= 150)
    price = models.FloatField()
    desctiption = models.TextField(default='')
    count = models.TextField(max_length=150)

# create table