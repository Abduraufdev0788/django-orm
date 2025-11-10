from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=128)
    catogory = models.CharField(max_length=128)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.IntegerField()
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    active = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Product(id={self.id}, name="{self.name}")'
    
