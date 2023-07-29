from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)


class Stock(models.Model):
    product = models.ForeignKey(
        Product, related_name="stocks", on_delete=models.CASCADE
    )
    cost = models.DecimalField(max_digits=10, decimal_places=2)