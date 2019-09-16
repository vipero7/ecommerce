from django.urls import path
from .import views

app_name = 'account'

urlpatterns = [
    path('', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),
]