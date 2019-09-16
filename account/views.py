from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from .forms import LoginForm
# Create your views here.

def user_login(request):
    if request.user.is_active:
        if request.user.is_staff:
            return render(request , 'account/admin/dashboard.html')
        else:
            return render(request , 'account/user/home.html')
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
                            return render(request , 'account/admin/dashboard.html')
                        else:
                            return render(request , 'account/user/home.html')
                    else:
                        return HttpResponse('Disabled Account')
                else:
                    return HttpResponse("Invalid Login")
        else:
            form = LoginForm()
        return render(request, 'account/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('/')