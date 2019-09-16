from django.shortcuts import render, get_object_or_404, redirect
from .forms import AddProductForm
from account.views import user_login
from product.models import Product

# Create your views here.
def home(request):
    return render(request, 'home.html')

def product_list(request):
    products = Product.objects.all()
    return render(request, 'account/admin/product_list.html', {'products': products})


def product_detail(request, id):
    return render(request, 'account/admin/product_detail.html')


def add_product(request):
    if request.method == POST:
        return
    else:
        form = AddProductForm()
    return render(request, 'account/admin/add_product.html', {'form': form})

def edit(request, id):
    return render(request, 'account/admin/product_detail.html')

def delete(request, id):
    # product = Product.get_object_or_404(id=id)
    # product.delete()
    return render(request, 'account/admin/product_detail.html')