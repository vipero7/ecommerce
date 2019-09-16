from django.urls import path
from . import views

app_name = 'product'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('add/', views.add_product, name='add_product'),
    path('<int:id>/', views.product_detail, name='product_detail'),
    path('<int:id>/edit', views.edit, name='edit_product'),
    path('<int:id>/delete', views.delete, name='delete_product'),
]