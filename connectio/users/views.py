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
        profile = request.user.profile
        context = {
            'image': profile.image.url,
            'name': profile.name,
            'bio': profile.bio,
            'events': [
                {
                    'title': 'Sudoku Night',
                    'date': '20-2-2022',
                    'description': "Let's play sudoku",
                    'location': 'Memorial Union',
                    'attendance_count': 420,
                    'cost': 'Free',
                    'capacity': 690,
                },
                {
                    'title': 'Bingo Night',
                    'date': '11-4-2022',
                    'description': "Let's play Bingo",
                    'location': 'Union South',
                    'attendance_count': 300,
                    'cost': '$12.50',
                    'capacity': 500,
                },
                {
                    'title': 'Concert',
                    'date': '5-5-2022',
                    'description': "Chainsmokers concert",
                    'location': 'Overture center',
                    'attendance_count': 1300,
                    'cost': '$50.00',
                    'capacity': 2500,
                },
            ]
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


def register_user(request, username, email, password, location, bio, *args, **kwargs):
    username = username.lower()
    email = email.lower()
    new_user = NewUser.objects.create_user(username, email, password)
    new_user.save()
    new_user.profile.location = location
    new_user.profile.bio = bio
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
