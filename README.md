# upload

## Dependencies
Python 3  
Virtualenv  
SQLite 3  

## Quickstart
```
virtualenv venv -p $(which python3)
. venv/bin/activate
pip install -r requirements.txt
./manage.py migrate
./manage.py runserver 8000
```

In your brower navigate to [localhost:8000/upload/](http://localhost:8000/upload/)

There you will find a simple (and unfortunately unstytled) form
that accepts a file upload.

Clicking upload will upload the file to the backend where
the file will be parsed, and any users/products/orders will be
created or updated.


## The Database
If you'd like to inspect the data from the command line you can
use SQLite 3.
```
sqlite 3
> select * from product_product;
> select * from customer_customer;
> select * from order_order;
```

## Moving Forward
1. Add view and form testing
2. Add authentication using Django's built in authentication
3. Increased validation of posted data
4. Add ability to upload large files by using something like S3
5. Add styling to the form, better error messages, etc.
6. Upload status, success, failure indication.
7. Viewing data in the app (easiest to use Django Admin)
