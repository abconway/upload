from decimal import Decimal

from django.test import TestCase

from .models import Product


class TestProductModel(TestCase):
    def test_create(self):
        Product.objects.create(
            name='A Product',
            purchase_amount=25.37,
        )

        product = Product.objects.first()

        self.assertEqual(product.name, 'A Product')
        self.assertAlmostEqual(product.purchase_amount, Decimal(25.37), places=2)
