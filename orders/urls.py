from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path('create/', views.order_create, name='order_create'),
    path('list/', views.order_list, name='order_list'),
    path('order_lists/', views.order_lists_admin, name='order_lists_admin'),
    path('<int:id>/edit', views.edit_order, name='edit_order'),
    path('<int:id>/delete', views.delete_order, name='delete_order'),
    path('<int:id>/', views.order_detail, name='order_detail'),
    path('<int:id>/update', views.update_order, name='update_order'),
    path('<int:id>/update_order_item', views.update_order_item, name='update_order_item'),
    path('<int:id>/delete_order_item', views.delete_order_item, name='delete_order_item'),
]