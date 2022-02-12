from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.


def home(request):
    context = {}
    return render(request, 'interface/home.html', context)


def create(request):
    context = {}
    return render(request, 'interface/create.html', context)


def date(request, date):
    context = {}
    return render(request, 'interface/date.html', context)


def all_events(request):
    context = {
        'events': Events.objects.all().order_by('date')
    }
    return render(request, 'interface/all_events.html', context)


@login_required(login_url='')
def messages(request):
    context = {}
    return render(request, 'interface/messages.html', context)


def about(request):
    context = {}
    return render(request, 'interface/about.html', context)


def ifdfa(request):
    context = {
        'site_title': 'Connectio',
    }
    return render(request, 'interface/base.html', context)
