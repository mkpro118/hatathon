from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create', views.create, name='create'),
    path('events', views.events, name='events'),
    path('about', views.about, name='about'),
    path('create_event/<str:t>&&<str:d>&&<str:l>&&<str:de>&&<str:ct>&&<str:cs>&&<str:cp>', views.CreateEvent, name='create_event'),
]
