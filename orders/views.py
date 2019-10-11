from django.shortcuts import render, redirect, get_object_or_404
from .models import OrderItem, UserOrders, Order
from .forms import OrderCreateForm, OrderEditForm
from cart.cart import Cart
from django.contrib.auth.models import User
from django.contrib.admin.views.decorators import staff_member_required
import pdb

# Create your views here.

def order_list(request):
    if request.user.is_authenticated:
        user = get_object_or_404(User, username=request.user.username)
        user_orders =  UserOrders.objects.filter(user_profile_id=user.profile)
        orders = []
        
        for items in user_orders:
            order_item = OrderItem.objects.filter(order=items.order_id)
            for i in order_item:
                orders.append(i)
        # pdb.set_trace()
        return render(request, 'account/orders/order_list.html', {'user': user, 'orders': orders})
    else:
        return redirect('/')

    

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
            return redirect('orders:order_list')
    else:
        form = OrderCreateForm()
    return render(request, 'account/orders/create.html', {'cart': cart, 'form': form})


@staff_member_required(login_url='/account')
def order_lists_admin(request):
    orders = Order.objects.all()
    return render(request, 'account/admin/order_list.html', {'orders': orders})

@staff_member_required(login_url='/account')
def edit_order(request, id):
    order = get_object_or_404(Order, id=id)
    form = OrderEditForm(instance=order)
    return render(request, 'account/admin/edit_order.html', {'form': form, 'order': order, 'order_item': order_item})


@staff_member_required(login_url='/account')
def update_order(request, id):
	order = Order.objects.get(id=id)
	form = OrderEditForm(request.POST, instance=order)
	if form.is_valid():
		form.save()
		return redirect('orders:order_lists_admin')
	return render(request, 'account/admin/edit_order.html', {'order': order})


@staff_member_required(login_url='/account')
def delete_order(request, id):
    order = Order.objects.get(id=id)
    order.delete()
    return redirect('orders:order_lists_admin')


@staff_member_required(login_url='/account')
def order_detail(request, id):
    order = get_object_or_404(Order, id=id)
    order_item = OrderItem.objects.filter(order=order)
    return render(request, 'account/admin/order_item_detail.html', {'order_item': order_item})