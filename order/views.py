from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponseRedirect

from customer.models import Customer
from customer.forms import CustomerForm
from product.models import Product
from product.forms import ProductForm

from .forms import UploadFileForm
from .models import Order


def get_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('/upload/')
    else:
        form = UploadFileForm()

    return render(request, 'order.html', {'form': form})


def handle_uploaded_file(f):
    for chunk in f.chunks():
        lines = chunk.decode('utf-8').split('\n')
        for line in lines:
            if len(line) > 0:
                items = line.split('\t')
                customer_form = CustomerForm({
                    'id': items[0],
                    'first_name': items[1],
                    'last_name': items[2],
                    'street_address_line': items[3],
                    'state': items[4],
                    'zip_code': items[5],
                })
                product_form = ProductForm({
                    'id': items[7],
                    'name': items[8],
                    'purchase_amount': items[9],
                })

                if customer_form.is_valid() and product_form.is_valid():
                    customer, _ = Customer.objects.get_or_create(**customer_form.data)
                    product, _ = Product.objects.get_or_create(**product_form.data)
                    order, _ = Order.objects.get_or_create(
                        customer=customer,
                        product=product,
                        defaults={
                            'date': datetime.now(),
                        }
                    )
                    order.status = items[6]
                    order.date = items[10]
                    order.save()
                else:
                    print(customer_form.errors)
                    print(product_form.errors)

