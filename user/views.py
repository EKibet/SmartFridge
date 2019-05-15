from django.shortcuts import render,redirect , get_object_or_404
from .models import *
from .forms import SettingsForm
from fridge.models import *
from user.models import *

from carton.cart import Cart

# Create your views here.
def home(request):
    supplies = Stock.objects.all()
    state = ShoppingCart.objects.all()
    return render(request,'home.html',locals())

def settings(request):
    stock = Stock.objects.all()
    settings = UserSetting.objects.all()
    settingform = SettingsForm()
    return render(request,'settings.html',locals())



def limiting(request, stock_id = None):
    stock = Stock.objects.get(pk=stock_id)

    if request.method == 'POST':
        settingform = SettingsForm(request.POST, request.FILES)
        print(settingform.errors)
        if settingform.is_valid():
            limit = settingform.save(commit=False)
            limit.product = stock
            limit.save()
            return redirect('home')
    else:
        settingform = SettingsForm()
    return render(request,'user-preference.html',locals())


def orders(request):
    cart = Cart(request.session)

    prods = [i.product for i in cart.items]

    nk = Kart.objects.create()
    for i in prods:
        nk.product.add(i)

    ordi = Order(cart=nk)
    ordi.save()

    # cart.clear()

    return redirect(receipt)
    # return render(request, 'auto/receipt.html', locals())



def supplier(request):
    orders = Order.objects.all()
    return render(request, 'auto/orders.html', locals())


def selected(request, item_id=None):
    x = Order.objects.get(pk=item_id)
    selected = Product.objects.filter(px__kx=x)
    return render(request, 'auto/order_details.html', locals())


def receipt (request):
    '''
    a receipt provided to show order has been made successfully . also send the owner an sms
    '''
    cart = Cart(request.session)

    # customer = get_object_or_404(Profile, user=request.user)
    products = ', '.join(i.product.name for i in cart.items)

    message = "Dear "+ 'budaboss'.upper() +", your order "+products+" KES:"+str( cart.total ) + \
        " ,has been processed ! Kindly , authorize cashout ."

    print ( message )
    # customer_number = '254'+str(customer.phone_number)
    customer_number = str(729309658)

    send_receipt(message, customer_number)

    copy = cart
    cart.clear()
    return render (request , 'auto/receipt.html' , locals())


def order_history (request):
    '''
    user will be taken to a page containig history of all order his/her fridge has made 
    '''

    return render( request , 'auto/history.html' ,locals() )