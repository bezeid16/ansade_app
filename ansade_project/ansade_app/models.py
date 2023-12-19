# ansade_app/models.py

from django.db import models

class ProductFamily(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    family = models.ForeignKey(ProductFamily, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
