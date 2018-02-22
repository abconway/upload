from django.db import models


class Order(models.Model):
    customer = models.ForeignKey('customer.Customer', on_delete='Cascade')
    product = models.ForeignKey('product.Product', on_delete='Cascade')
    status = models.CharField(
        max_length=64,
        choices=(
            ('new', 'New'),
            ('canceled', 'Canceled'),
        ),
    )
    date = models.DateTimeField()
