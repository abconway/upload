from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=256)
    purchase_amount = models.DecimalField(max_digits=8, decimal_places=2)
