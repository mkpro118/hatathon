from django.urls import path
from . import views

urlpatterns = [
    path('login', views.Login, name='login'),
    path('logout', views.Logout, name='logout'),
    path('register', views.Register, name='register'),
    path('edit/<str:name>&&<str:email>&&<str:bio>&&<str:location>', views.Edit, name='edit'),
    path('profile', views.DefaultProfile),
    path('profile/<str:username>', views.Profile, name='profile'),
    path('check_username_availablility/<str:username>',
         views.check_username_availability,
         name='check-username-availability'),
    path('check_email_availablility/<str:email>',
         views.check_email_availability,
         name='check-email-availability'),
    path('register_user/<str:username>&<str:email>&<str:password>&<str:location>&<str:bio>',
         views.register_user,
         name='register-user'),
    path('login_user/<str:username>&<str:password>',
         views.login_user,
         name='login-user')
]
