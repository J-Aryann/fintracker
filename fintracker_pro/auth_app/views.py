from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout

# Create your views here.

def registration_view(request):
    template_name='auth_app/login.html'
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('signin_url')
    context ={'form':form}
    return render(request,template_name,context)


def signin_view(request):
    template_name='auth_app/signin.html'
    if request.method=='POST':
        user_name = request.POST.get('username')
        passw = request.POST.get('password')
        print(user_name,passw)
        user= authenticate(request,username=user_name,password=passw)
        print('USER',user)
        if user:
            login(request,user)
            return redirect('create_investment_url')
    return render(request,template_name)


def logout_view(request):
    logout(request)
    return redirect('signin_url')