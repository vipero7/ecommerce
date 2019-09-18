from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from .forms import AddProductForm, ProductEditForm
from account.views import user_login
from product.models import Product

# Create your views here.
def home(request):
    return render(request, 'home.html')

def product_list(request):
    products = Product.objects.all()
    return render(request, 'account/admin/product_list.html', {'products': products})
    
def add_product(request):
    if request.method == 'POST':
        form = AddProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/product')
    else:
        form = AddProductForm()
    return render(request, 'account/admin/add_product.html', {'form': form})

def edit(request, id):
    product = get_object_or_404(Product, id=id)
    form = AddProductForm(instance=product)
    return render(request, 'account/admin/edit_product.html', {'form': form, 'product': product})


def update(request, id):
	product = Product.objects.get(id=id)
	form = AddProductForm(request.POST, request.FILES, instance=product)
	if form.is_valid():
		form.save()
		return redirect('/product')
	return render(request, 'account/admin/edit_product.html', {'product': product})

def delete(request, id):
    product = Product.objects.get(id=id)
    product.delete()
    return redirect('/product')