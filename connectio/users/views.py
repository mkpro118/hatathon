from django.shortcuts import (render,
                              # HttpResponse,
                              redirect,)
from django.http import JsonResponse
from .models import NewUser
from django.contrib.auth.decorators import login_required

from django.contrib.auth import login, authenticate, logout


# Create your views here.


def Register(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        return render(request, 'users/register.html', {})


def Login(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        return render(request, 'users/login.html', {})


@login_required(login_url='login')
def Logout(request):
    logout(request)
    return render(request, 'users/logout.html', {})


@login_required(login_url='login')
def Profile(request):
    if request.method == 'POST':
        return redirect('profile')
    else:
        context = {
            'image': request.user.profile.image.url,
            'name': request.user.profile.name,
        }
        return render(request, 'users/profile.html', context)


def check_username_availability(request, username):
    username_to_check = username
    taken = NewUser.is_username_taken(username_to_check)
    return JsonResponse({'taken': taken})


def check_email_availability(request, email):
    email_to_check = email
    taken = NewUser.is_email_taken(email_to_check)
    return JsonResponse({'taken': taken})


def register_user(request, username, email, password, *args, **kwargs):
    username = username.lower()
    email = email.lower()
    new_user = NewUser.objects.create_user(username, email, password)
    new_user.save()
    account = authenticate(username=username, password=password)
    login(request, account)
    destination = kwargs.get('next')
    if destination:
        return JsonResponse({'next': destination})
    else:
        return JsonResponse({'next': ''})


def login_user(request, username, password, *args, **kwargs):
    account = authenticate(username=username, password=password)
    if account is not None:
        login(request, account)
        nxt = kwargs.get('next')
        if nxt:
            return JsonResponse({'successful': True, 'next': nxt})
        else:
            return JsonResponse({'successful': True, 'next': ''})
    else:
        taken = NewUser.is_username_taken(username)
        if taken:
            return JsonResponse({'successful': False, 'username_valid': taken, 'password_valid': False})
        else:
            return JsonResponse({'successful': False, 'username_valid': taken, 'password_valid': True})
