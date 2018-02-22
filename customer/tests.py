from django.test import TestCase

from .models import Customer


class TestCustomerModel(TestCase):
    def test_create(self):
        Customer.objects.create(
            first_name='Staypuff',
            last_name='Marshmallow',
            street_address_line_1='123 Some Rd',
            street_address_line_2='Apt 3E',
            state='AZ',
            zip_code='23232',
        )

        customer = Customer.objects.first()

        self.assertEqual(customer.first_name, 'Staypuff')
        self.assertEqual(customer.last_name, 'Marshmallow')
        self.assertEqual(customer.street_address_line_1, '123 Some Rd')
        self.assertEqual(customer.street_address_line_2, 'Apt 3E')
        self.assertEqual(customer.state, 'AZ')
        self.assertEqual(customer.zip_code, '23232')
