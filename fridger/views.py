from django.shortcuts import render,redirect,get_object_or_404
from django.shortcuts import render,redirect,get_object_or_404

from .models import *
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm,ItemModelForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from carton.cart import Cart

import csv


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

    return render(request, 'users/register.html',{'form': form})


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
    print(request.session.session_key)
    print(request)

    s_key = request.session.session_key

    # ******************************
    # ****** Let's write the session key to a csv **********

    with open('session_key.csv', 'w') as f:
        s_key = s_key.rsplit(',')
        print(s_key)
        writer = csv.writer(f)
        writer.writerow( s_key ) 



    product = Product.objects.get(id=item_id)
    cart.add(product, price=product.selling_price)

    return redirect('stock')


def remove(request, item_id):
    '''
    Controller function for removing an item from the cart.
    '''
    cart = Cart(request.session)
    product = Product.objects.get(id=item_id)
    # cart.remove(product, price=product.selling_price)
    cart.remove(product)
    return render(request, 'cart.html', locals())


def show(request):
    cart = Cart(request.session)
    # stock = Product.objects.all()
    total=cart.total
    # subtotal=cart.subtotal()

    return render(request, 'cart.html',locals())    

def single_item(request,item_id):

    item = get_object_or_404(Product,pk=item_id)

    return render(request,'single_cart.html',locals())
