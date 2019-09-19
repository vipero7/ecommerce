from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from .forms import AddCategoryForm, AddProductForm, ProductEditForm
from account.views import user_login
from product.models import Category, Product


#Home View
def home(request):
    return render(request, 'account/user/home.html')


#Category Views
def category_list(request):
    categories = Category.objects.all()
    return render(request, 'account/admin/category_list.html', {'categories': categories})


def add_category(request):
    if request.method == 'POST':
        form = AddCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product:category_list')
        else:
            return HttpResponse('Could Not Update')
    else:
        form = AddCategoryForm()
    return render(request, 'account/admin/add_category.html', {'form': form})

def edit_category(request, id):
    category = get_object_or_404(Category, id=id)
    form = AddCategoryForm(instance=category)
    return render(request, 'account/admin/edit_category.html', {'form': form, 'category': category})

def update_category(request, id):
    category = Category.objects.get(id=id)
    form = AddCategoryForm(request.POST, instance=category)
    if form.is_valid():
        form.save()
        return redirect('product:category_list')
    return render(request, 'account/admin/edit_category.html', {'form': form, 'category': category})


def delete_category(request, id):
    category = Category.objects.get(id=id)
    category.delete()
    return redirect('product:category_list')
        

# Product Views.
def product_list(request):
    products = Product.objects.all()
    return render(request, 'account/admin/product_list.html', {'products': products})
    
def add_product(request):
    if request.method == 'POST':
        form = AddProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product:product_list')
    else:
        form = AddProductForm()
    return render(request, 'account/admin/add_product.html', {'form': form})

def edit_product(request, id):
    product = get_object_or_404(Product, id=id)
    form = AddProductForm(instance=product)
    return render(request, 'account/admin/edit_product.html', {'form': form, 'product': product})


def update_product(request, id):
	product = Product.objects.get(id=id)
	form = AddProductForm(request.POST, request.FILES, instance=product)
	if form.is_valid():
		form.save()
		return redirect('product:product_list')
	return render(request, 'account/admin/edit_product.html', {'product': product})

def delete_product(request, id):
    product = Product.objects.get(id=id)
    product.delete()
    return redirect('product:product_list')
