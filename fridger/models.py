from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

from multiprocessing import Process


class Profile(models.Model):

    profile_path = models.ImageField(
        upload_to='profile_pics/', default='profile_pics/default.jpg')
    bio = models.TextField()
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return f'{self.user.username} Profile'


class Product(models.Model):
    name = models.CharField(max_length=64)
    quantity = models.PositiveIntegerField()
    item_path = models.ImageField(upload_to='food_items/')
    item_path2 = models.ImageField(upload_to='food_items/', null=True)

    selling_price = models.DecimalField(max_digits=18, decimal_places=2)
    supply_date = models.DateTimeField()

    def __str__(self):
        return f'{self.name}'

    def total_price(self):
        return self.quantity * self.unit_price
    total_price = property(total_price)

    def get_product(self):
        return self.content_type.get_object_for_this_type(pk=self.object_id)

    def set_product(self, product):
        self.content_type = ContentType.objects.get_for_model(type(product))
        self.object_id = product.pk

    product = property(get_product, set_product)


class Stock(models.Model):
    product = models.ForeignKey(Product)
    current_qty = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.product.name}s in stock"


class ShoppingCart(models.Model):
    product = models.ForeignKey(Product)
    quantity = models.PositiveIntegerField()

    def add_limit(self):
        self.add()

    def remove_limit(self):
        self.delete()


# def call_tensor():
#     import tensorflow as tf

#     from utils import backbone
#     from api import object_counting_api
#     import cv2
#     from carton.cart import Cart

#     input_video = 0
#     detection_graph, category_index = backbone.set_model(
#         'faster_rcnn_inception_v2_coco_2018_01_28')

#     # (for counting targeted objects) change it with your targeted objects
#     targeted_objects = "banana"
#     fps = 24  # change it with your input video fps
#     width = 854  # change it with your input video width
#     height = 480  # change it with your input vide height
#     is_color_recognition_enabled = 0

#     object_counting_api.targeted_object_counting(input_video, detection_graph, category_index,
#                                                  is_color_recognition_enabled, targeted_objects, fps, width, height)  # targeted objects counting


# # Process(target=call_tensor).start()


# def waiter():
#     while True:
#         from fridge.models import ShoppingCart, Product
#         from django.contrib.sessions.backends.db import SessionStore
#         from user.models import UserSetting

#         import tensorflow as tf
#         import csv

#         from utils import backbone
#         from api import object_counting_api
#         import cv2
#         from carton.cart import Cart

#         # Open a csv file where the session key has been appended
        
#         with open('session_key.csv', 'r') as f:
#             data = csv.reader(f)
#             for line in data:
#                 k =  line
#             k = k[0]

#         s = SessionStore(session_key=k)

#         cart = Cart(s)


#         product = Product.objects.get(name='Avocado')
#         print(product)

#         with open('object_counting_report.csv', 'r') as reading:
#             read = csv.reader(reading)
#             for line in read:
#                 for l in line:
#                     name = []
#                     number = []
#                     for item in l:
#                         if item.isalpha():
#                             name.append(item)
#                         elif item.isdigit():
#                             number.append(int(item))
#                         else:
#                             pass
#                     name = (''.join(c for c in name))
#                     number = (number[0])
#                     prodset = UserSetting.objects.all()

#                     for item in prodset:
#                         if number < item.limit:

#                             qty = item.limit-number
#                             try:
#                                 # tobeupdated = ShoppingCart.objects.get(product=item.product)
#                                 product = Product.objects.get(name='Avocado')

#                                 # cart.add( product )
#                                 cart.add(product, price=product.selling_price)
#                                 print ( cart.items ) 

#                             except:
#                                 # cart = ShoppingCart(product=item.product, quantity=qty)
#                                 print('excepted')
#                                 # pass

#         break


# Process(target=waiter).start()
# sam.ngigi@moringaschool.com

