from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm

from .forms import RegisterForm

class Landing(View):
    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, 'landing/landing.html', context)

class Login(View):
    def get(self, request, *args, **kwargs):
        form = AuthenticationForm()
        context = {'form' : form}
        return render(request, 'landing/login.html', context)

    def post(self, request, *args, **kwargs):
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')

        context = {'form' : form}
        return render(request, 'landing/login.html', context)

class Register(View):
    def get(self, request, *args, **kwargs):
        form = RegisterForm()
        context = {'form' : form}
        return render(request, 'landing/register.html', context)

    def post(self, request, *args, **kwargs):
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

        context = {'form' : form}
        return render(request, 'landing/register.html', context)

class Logged_out(View):
    def post(self, request, *args, **kwargs):
        logout(request)
        return redirect('logout_page')

class Logout_page(View):
    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, 'landing/logout_page.html', context)

class About(View):
    def get(self, request,*args, **kwargs):
        context = {}
        return render(request, 'landing/about.html', context)