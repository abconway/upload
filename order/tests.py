from datetime import datetime, timezone

from django.test import TestCase

from customer.models import Customer
from product.models import Product

from .models import Order


class TestOrderModel(TestCase):
    def test_create(self):
        customer = Customer.objects.create(
            first_name='Staypuff',
            last_name='Marshmallow',
            street_address_line='123 Some Rd',
            state='AZ',
            zip_code='23232',
        )

        product = Product.objects.create(
            name='A Product',
            purchase_amount=25.37,
        )

        now = datetime.now(tz=timezone.utc)
        Order.objects.create(
            customer=customer,
            product=product,
            status='new',
            date=now,
        )

        order = Order.objects.first()

        self.assertEqual(order.date, now)
        self.assertEqual(order.status, 'new')
        self.assertEqual(order.customer, customer)
        self.assertEqual(order.product, product)
