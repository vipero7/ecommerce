from django.urls import path
from . import views

app_name = 'product'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('add/', views.add_product, name='add_product'),
    path('<int:id>/edit', views.edit_product, name='edit_product'),
    path('<int:id>/update', views.update_product, name='update_product'),
    path('<int:id>/delete', views.delete_product, name='delete_product'),
    path('categories/', views.category_list, name='category_list'),
    path('categories/add/', views.add_category, name='add_category'),
    path('categories/<int:id>/edit', views.edit_category, name='edit_category'),
    path('categories/<int:id>/update', views.update_category, name='update_category'),
    path('categories/<int:id>/delete', views.delete_category, name='delete_category'),
    path('<slug:product>/', views.product_detail, name='product_detail')
]
