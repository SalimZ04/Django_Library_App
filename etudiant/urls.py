from os import name
from django.urls import path
from . import views


urlpatterns=[
    path('home',views.home,name='home'),
    path('listethese/<int:id>',views.listethese,name='listethese'),
    path('these/<int:id>',views.these,name='these'),
]