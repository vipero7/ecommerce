from django.shortcuts import render, redirect
from .models import OrderItem, UserOrders
from .forms import OrderCreateForm
from cart.cart import Cart
import pdb

# Create your views here.

def order_list(request):
    return render(request, 'account/orders/order_list.html')

def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            if request.user.is_authenticated:
                UserOrders.objects.create(user_profile_id=request.user.profile, order_id=order)
            for item in cart:
                OrderItem.objects.create(order=order, product=item['product'], price=item['price'], quantity=item['quantity'])

            cart.clear()
            return redirect(request, 'orders:order_list', {'order': order})
    else:
        form = OrderCreateForm()
    return render(request, 'account/orders/create.html', {'cart': cart, 'form': form})