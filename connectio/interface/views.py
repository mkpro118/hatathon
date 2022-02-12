from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Events

# Create your views here.


def home(request):
    events = Events.objects.all().order_by('-attendance_count')
    events = events[:5] if len(events) > 5 else events
    context = {
        'site_title': 'Connectio',
        'events': events,
    }
    return render(request, 'interface/home.html', context)


def create(request):
    context = {
        'site_title': 'Create Event - Connectio',
    }
    return render(request, 'interface/create.html', context)


def events(request):
    context = {
        'site_title': 'Events - Connectio',
        'events': Events.objects.all().order_by('date')
    }
    return render(request, 'interface/events.html', context)


def about(request):
    context = {
        'site_title': 'About - Connectio',
    }
    return render(request, 'interface/about.html', context)


@login_required(login_url='login')
def CreateEvent(request, t, d, l, de, ct, cs, cp):
    event = Events(title=t, date=d, location=l, attendance_count=ct, description=de, cost=cs, capacity=cp, host=request.user)
    event.save()
    return JsonResponse({'next': 'profile'})
