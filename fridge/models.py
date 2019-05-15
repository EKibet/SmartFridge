from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
import csv
from multiprocessing import Process
from carton.cart import Cart
from django.shortcuts import render,redirect,get_object_or_404


class Profile(models.Model):
    
    profile_path = models.ImageField(upload_to = 'profile_pics/',default='profile_pics/default.jpg')
    bio = models.TextField()
    user = models.OneToOneField(User,on_delete=models.CASCADE, primary_key=True)
    def __str__(self):
        return f'{self.user.username} Profile'    
# class UserPreferences(models.Model):
#     prod_name = models.ForeignKey(Product)    
#     set_limit =  models.PositiveIntegerField()
#     usr = models.ForeignKey(Profile)
  
#     def __str__(self):
#         return f'{self.prod_name}'   
# def waiter():
#     while True:
#         prodset = Product.objects.all()
#         for num in prodset:
#             if num.set_limit <= 7:
#                 print('order')              
#         continue  
    
# Process(target=waiter).start()



# class Cart(models.Model):
#     creation_date = models.DateTimeField(verbose_name=_('creation date'))
#     checked_out = models.BooleanField(default=False, verbose_name=_('checked out'))

#     class Meta:
#         verbose_name = _('cart')
#         verbose_name_plural = _('carts')
#         ordering = ('-creation_date',)

#     def __unicode__(self):
#         return unicode(self.creation_date)


class Product(models.Model):
    name = models.CharField(max_length=64)
    quantity = models.PositiveIntegerField()
    item_path = models.ImageField(upload_to = 'food_items/')
    item_path2 = models.ImageField(upload_to = 'food_items/',null=True)

    selling_price = models.DecimalField(max_digits=18, decimal_places=2)
    supply_date = models.DateTimeField()
    discount = models.PositiveIntegerField()
    buying_price = models.PositiveIntegerField()
    remaining = models.PositiveIntegerField()


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



class UserLimit(models.Model):
    # name = models.CharField(max_length=64)
    product = models.ForeignKey(Product)
    set_limit = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.product.name}'s limit"
    
    def add_limit(self):
        self.add()
    
    def remove_limit(self):
        self.delete()

class ShoppingCart(models.Model):
    product = models.ForeignKey(Product)
    quantity = models.PositiveIntegerField()
    read = models.BooleanField(default=False)
    total = models.PositiveIntegerField()
    
    
def orders(request):
    cart = Cart(request.session)

    prods =[i.product for i in cart.items]
    
    nk = Kart.objects.create()
    for i in prods:
        nk.product.add(i)

   
    ordi = Order(nk)
    

    return render(request,'index.html',locals())

def single_item(request,item_id):

    item = get_object_or_404(Product,pk=item_id)

    return render(request,'single_cart.html',locals())


def supplier(request):
    orders = Order.objects.all()
    return render(request,'supply.html',locals())

def selected(request,item_id=None):
   
    x = Order.objects.get(pk=item_id)
    selected = Product.objects.filter(px__kx=x)
    
  
    return render(request,'the_order.html',locals())


