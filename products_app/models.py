from django.db import models

class Company(models.Model):
    id = models.AutoField(max_length=20, unique=True, default='000000000', primary_key=True) # type: ignore
    name = models.CharField(max_length=255) # type: ignore

    def __str__(self):
        return self.name

class Warehouse(models.Model):
    id = models.AutoField(max_length=10, unique=True, default=0000000000, primary_key=True) # type: ignore
    name = models.CharField(max_length=255) # type: ignore

    def __str__(self):
        return self.name

class Product(models.Model):
    id = models.AutoField(max_length=10, unique=True, default=0000000000, primary_key=True) # type: ignore
    name = models.CharField(max_length=250) # type: ignore
    amount = models.IntegerField() # type: ignore
    measure = models.CharField(max_length=20) # type: ignore

    def __str__(self):
        return self.name