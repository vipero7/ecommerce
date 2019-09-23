from django.urls import path
from .import views

app_name = 'account'

urlpatterns = [
    path('', views.admin_dashboard, name='admin_dashboard'),
    path('admin/login/', views.admin_login, name='admin_login'),
    path('admin/logout/', views.admin_logout, name='admin_logout'),
]