from django.urls import path

from . import views

urlpatterns = [
    path('chat', views.home, name='chat-home'),
    path('chat/<str:group>', views.chat, name='chat'),
]
