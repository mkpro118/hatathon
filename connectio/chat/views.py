from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# from django.http import JsonResponse
from django.http import HttpResponse

from .models import Group, Message
from users.models import NewUser
# Create your views here.


@login_required
def chat(request, group):
    try:
        normalized = group.replace(request.user.username, '')
        if normalized[0] == '_':
            normalized = normalized[1:]
        elif normalized[-1] == '_':
            normalized = normalized[:-1]
        group = normalized
        validate_member1 = NewUser.objects.get(username=group)
    except Exception:
        return HttpResponse(f"<h1>User {group} does not exist</h1>")
    try:
        group_name = Group.objects.get(group_name=f'{group}_{request.user.username}')
    except Exception:
        try:
            group_name = Group.objects.get(group_name=f'{request.user.username}_{group}')
        except Exception:
            group_name = Group(group_name=f'{group}_{request.user.username}')
            group_name.save()
            group_name.members.add(request.user, validate_member1)
            group_name.save()

    messages = Message.objects.filter(group=group_name).order_by('-time')
    groups = Group.objects.filter(members=request.user)

    context = {
        'user': request.user,
        'other': normalized,
        'image': request.user.profile.image.url,
        'messages': messages,
        'groups': groups,
        'this': group_name,
    }
    return render(request, 'chat/chat.html', context=context)


@login_required
def home(request):
    groups = Group.objects.filter(members=request.user)
    context = {
        'user': request.user,
        'image': request.user.profile.image.url,
        'groups': groups,
    }
    return render(request, "chat/home.html", context=context)
