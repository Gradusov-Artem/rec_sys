from django.db import models

class Company(models.Model):
    id = models.CharField(max_length=20, unique=True, default='000000000', primary_key=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name