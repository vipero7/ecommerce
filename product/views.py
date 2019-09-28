from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from .forms import AddCategoryForm, AddProductForm, ProductEditForm
from product.models import Category, Product
from django.contrib.admin.views.decorators import staff_member_required
import pdb
#Home View
def home(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    return render(request, 'account/home.html', {'products': products, 'categories': categories})


#Category Views
@staff_member_required(login_url='/account')
def category_list(request):
    categories = Category.objects.all()
    return render(request, 'account/admin/category_list.html', {'categories': categories})

@staff_member_required(login_url='/account')
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

@staff_member_required(login_url='/account')
def edit_category(request, id):
    category = get_object_or_404(Category, id=id)
    form = AddCategoryForm(instance=category)
    return render(request, 'account/admin/edit_category.html', {'form': form, 'category': category})


@staff_member_required(login_url='/account')
def update_category(request, id):
    category = Category.objects.get(id=id)
    form = AddCategoryForm(request.POST, instance=category)
    if form.is_valid():
        form.save()
        return redirect('product:category_list')
    return render(request, 'account/admin/edit_category.html', {'form': form, 'category': category})

@staff_member_required(login_url='/account')
def delete_category(request, id):
    category = Category.objects.get(id=id)
    category.delete()
    return redirect('product:category_list')
        

# Product Views.
@staff_member_required(login_url='/account')
def product_list(request):
    products = Product.objects.all()
    return render(request, 'account/admin/product_list.html', {'products': products})

@staff_member_required(login_url='/account')
def add_product(request):
    if request.method == 'POST':
        form = AddProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product:product_list')
    else:
        form = AddProductForm()
    return render(request, 'account/admin/add_product.html', {'form': form})

@staff_member_required(login_url='/account')
def edit_product(request, id):
    product = get_object_or_404(Product, id=id)
    form = AddProductForm(instance=product)
    return render(request, 'account/admin/edit_product.html', {'form': form, 'product': product})


@staff_member_required(login_url='/account')
def update_product(request, id):
	product = Product.objects.get(id=id)
	form = AddProductForm(request.POST, request.FILES, instance=product)
	if form.is_valid():
		form.save()
		return redirect('product:product_list')
	return render(request, 'account/admin/edit_product.html', {'product': product})


@staff_member_required(login_url='/account')
def delete_product(request, id):
    product = Product.objects.get(id=id)
    product.delete()
    return redirect('product:product_list')


def product_detail(request, product):
    product = get_object_or_404(Product, name=product)
    return render(request, 'account/product_detail.html', {'product': product})

