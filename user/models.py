# from decouple import config, Csv
# import africastalking as af
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from multiprocessing import Process
from fridge.models import *

class UserSetting(models.Model):
    product = models.ForeignKey(Product)
    limit = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.product.product.name}'s limit"


class Kart(models.Model):
    product = models.ManyToManyField(Product, related_name='px')

    def __str__(self):
        return f'{self.pk} cart'


class Order(models.Model):
    cart = models.ForeignKey(Kart, related_name="kx")
    order_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.pk} Order'



# def send_receipt(message, customer):
#     # Initialize SDK
#     username = config('SUSERNAME')
#     api_key = config('SULEA_KEY')

#     af.initialize(username, api_key)

#     # Initialize a service e.g. SMS
#     receipt = af.SMS
#     # Use the service synchronously

#     customers = [
#         # "+"+customer,
#         '+254729309658',

#     ]

#     response = receipt.send(message, customers)
#     print(response)

#     # Or use it asynchronously

#     def on_finish(error, response):
#         if error is not None:
#             raise error
#         # print(response)
#         return response

#     # sms.send(message, ["+"+customer], callback=on_finish)
