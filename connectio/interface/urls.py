from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create', views.create, name='create'),
    path('messages', views.messages, name='messages'),
    path('date/<str:date>', views.date, name='date'),
    path('events', views.all_events, name='all_events'),
    path('events/<str:event>', views.events, name='events'),
    path('about', views.about, name='about'),
]
