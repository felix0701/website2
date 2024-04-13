from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('feed/', views.feed, name='feed'),
    path('signout/', views.signout, name='signout'),
    path('choose_options/', views.choose_options, name='choose_options'),
    path('message/', views.message, name='message'),
    path('mainpage/', views.mainpage, name='mainpage'),
    path('fill_details/', views.fill_details, name='fill_details'),
    
]
