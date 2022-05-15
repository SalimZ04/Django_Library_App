from os import name
from django.urls import path
from . import views


urlpatterns=[
    path('',views.home,name='home'),
    path('loginadd',views.loginadd,name='loginadd'),
    path('loginetd',views.loginetd,name='loginetd'),
    path('DeconnecterEtd',views.DeconnecterEtd,name='DeconnecterEtd'),
    path('DeconnecterAdd',views.DeconnecterAdd,name='DeconnecterAdd'),
]