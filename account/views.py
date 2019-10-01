from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from .forms import LoginForm, UserLoginForm, UserRegisterForm, UserEditForm, ProfileEditForm
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.contrib.auth.models import User
import pdb
# Create your views here.


@staff_member_required(login_url='account:admin_login')
def admin_dashboard(request):
    return render(request , 'account/admin/dashboard.html')


def admin_login(request):
    if request.user.is_staff:
        return render(request , 'account/admin/dashboard.html')
    else:
        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                cd = form.cleaned_data
                user = authenticate(request, username=cd['username'], password=cd['password'])
                if user is not None:
                    if user.is_active:
                        login(request, user)
                        if user.is_staff:
                            return redirect('account:admin_dashboard')
                        else:
                            return redirect('/login')
                    else:
                        return HttpResponse('Disabled Account')
                else:
                    return HttpResponse("Invalid Login")
        else:
            form = LoginForm()
        return render(request, 'account/admin/login.html', {'form': form})


def admin_logout(request):
    logout(request)
    return redirect('account:admin_login')


def user_login(request):
    if request.user.is_active:
        return redirect('home')
    else:
        if request.method == 'POST':
            form = UserLoginForm(request.POST)
            if form.is_valid():
                cd = form.cleaned_data
                user = authenticate(request, username=cd['username'], password=cd['password'])
                if user is not None:
                    if user.is_active:
                        login(request, user)
                        return redirect('home')
                    else:
                        return HttpResponse('Disabled Account')
                else:
                    return HttpResponse("Invalid Login")
        else:
            form = UserLoginForm()
        return render(request, 'account/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('/login')


def user_registration(request):
    if request.user.is_active:
        return HttpResponse('Please Log Out to Register')
    if request.method == 'POST':
        user_form = UserRegisterForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            login(request, new_user)
            pdb.set_trace()
            Profile.objects.create(user=new_user)
            return redirect('home')
    else:
        user_form = UserRegisterForm()
    return render(request, 'account/login.html', {'user_form': user_form})


@login_required(login_url='user_login')
def user_profile(request, username):
    user = get_object_or_404(User, username=username)
    if request.user.username == user.username:
        return render(request, 'account/user/profile.html', {'user': user})
    else:
        return HttpResponse("You are not Authorized")

