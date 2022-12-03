from django.shortcuts import render, redirect
from users.forms import *
from users.utils import get_user_from_request
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User


def login_page(requests):
    if requests.method == 'GET':
        data = {
            'form': LoginForm,
            'user': get_user_from_request(requests)
        }
        return render(requests, 'users/login.html', context=data)
    if requests.method == 'POST':
        form = LoginForm(data=requests.POST)

        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data.get('username'),
                password=form.cleaned_data.get('password')
            )

            if user:
                login(requests, user)
                return redirect('/products')
            else:
                form.add_error('username', 'bad request')

        data = {
            'form': form
        }
        return render(requests, 'users/login.html', context=data)


def logout_page(requests):
    logout(requests)
    return redirect('/products')


def register_page(requests):
    if requests.method == 'GET':
        data = {
            'form': RegisterForm
        }
        return render(requests, 'users/register.html', context=data)

    if requests.method == 'POST':
        form = RegisterForm(data=requests.POST)

        if form.is_valid():
            if form.cleaned_data.get('password1') == form.cleaned_data.get('password2'):
                user = User.objects.create_user(
                    username=form.cleaned_data.get('username'),
                    password=form.cleaned_data.get('password1')
                )
                login(requests, user)
                return redirect('/products')
            else:
                form.add_error('password1', 'password do not match!')
        data = {
            'form': form
        }
        return render(requests, 'users/register.html', context=data)
