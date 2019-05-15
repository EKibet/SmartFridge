from django.shortcuts import render,redirect,get_object_or_404

from .models import *
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm,ItemModelForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib import sessions
from carton.cart import Cart
from multiprocessing import Process
from django.contrib.sessions.backends.db import SessionStore


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!,You can now login')
            return redirect('login')
    else:
        form = UserRegisterForm()

    return render(request, 'users/login.html',{'form': form})


@login_required(login_url='/login/')
def profile(request):

    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm()

    context = {
        'u_form': u_form,
        'p_form': p_form,
    }

    return render(request, 'users/profile.html', context)

@login_required(login_url='/login/')
def watch_stock(request):
    s_key = request.session.session_key

    # ******************************
    # ****** Let's write the session key to a csv **********

    with open('session_key.csv', 'w') as f:
        s_key = s_key.rsplit(',')
        print(s_key)
        writer = csv.writer(f)
        writer.writerow( s_key ) 


    stock = Product.objects.all()
    return render(request,'index.html',locals())


def add(request,item_id):
    cart = Cart(request.session)
    product = Product.objects.get(id=item_id)
    cart.add(product, price=product.selling_price)
    return redirect('stock')
def adm(request):
    s_cart=ShoppingCart.objects.all()

    return render(request,'admin_orders.html',locals())    
def show(request):
    cart = Cart(request.session)
    # stock = Product.objects.all()
    total=cart.total
    # subtotal=cart.subtotal()
    # print(cart.items)
    s = SessionStore(request.session.session_key)
    print(s)

    # product = Product.objects.get(name='Avocado')
    # print(product)
    # cart = Cart(s)
    return render(request, 'cart.html',locals())    

def single_item(request,item_id):

    item = get_object_or_404(Product,pk=item_id)

    return render(request,'single_cart.html',locals())



def showcheck(request):
    all_cart = ShoppingCart.objects.all()
    return render(request,'check.html',locals())

# def view_your_fridge(request):

def call_tensor():
    import tensorflow as tf

    from utils import backbone
    from api import object_counting_api
    import cv2
    from carton.cart import Cart
    # from carton.cart import 
    input_video = 1
    detection_graph, category_index = backbone.set_model('faster_rcnn_inception_v2_coco_2018_01_28')

    targeted_objects =  "person"# (for counting targeted objects) change it with your targeted objects
    fps = 24 # change it with your input video fps
    width = 854 # change it with your input video width
    height = 480 # change it with your input vide height
    is_color_recognition_enabled = 0

    object_counting_api.targeted_object_counting(input_video, detection_graph, category_index, is_color_recognition_enabled, targeted_objects, fps, width, height) # targeted objects counting


Process(target=call_tensor).start()

def waiter():
    while True:
        from fridge.models import ShoppingCart,UserLimit,Product
        from carton.cart import Cart
        from django.contrib.sessions.backends.db import SessionStore

        with open('session_key.csv', 'r') as f:
            data = csv.reader(f)
            for line in data:
                k =  line
            k = k[0]

        s = SessionStore(session_key=k)

        cart = Cart(s)


        product = Product.objects.get(name='Avocado')
        print(product)
        with open('object_counting_report.csv' ,'r') as reading:
            read = csv.reader(reading)
            for line in read:
                for l in line:
                    name = []
                    number = []
                    for item in l:
                        if item.isalpha():
                            name.append(item)
                        elif item.isdigit():
                            number.append(int(item))
                        else:
                            pass
                    name = (''.join(c for c in name) )
                    number= (number[0])
                    prodset = UserLimit.objects.all()
                    # session = requests.Session()

                    for num in prodset:
                        if number <  num.set_limit:
                            qty = num.set_limit-number+1
                            print('dddddddddddddddddddddddddddddddddddddddddddd')
                            print(num.set_limit)
                        
                            try:
                                # tobeupdated = ShoppingCart.objects.get(product=item.product)
                                product = Product.objects.get(name='Avocado')

                                # cart.add( product )
                                cart.add(product, price=product.selling_price)
                                s.save()
                                print('paint')
                                print ( cart.items ) 
                                print('adding')

                            except:
                                # cart = ShoppingCart(product=item.product, quantity=qty)
                                print('excepted')
                                # pass
        break  
Process(target=waiter).start()    