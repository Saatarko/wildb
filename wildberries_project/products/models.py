from django.db import models

class Product(models.Model):
    article = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=255)
    brand = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=5, decimal_places=2)
    stock_quantity = models.IntegerField()
    warehouses = models.JSONField()  # Хранение информации по складам

    def __str__(self):
        return self.name