from django.db import models

from localflavor.us.models import USStateField, USZipCodeField, STATE_CHOICES


class Customer(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    street_address_line_1 = models.CharField(max_length=256)
    street_address_line_2 = models.CharField(max_length=256)
    state = USStateField(max_length=2, choices=STATE_CHOICES)
    zip_code = USZipCodeField()
