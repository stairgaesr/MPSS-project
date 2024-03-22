
from django.contrib import admin
from django.urls import path
from login_signup import views
#from shop_owner import views
#import pymongo 


urlpatterns = [
    path('', views.login, name = "login"),
    path('owner_home', views.owner_home, name ="owner_home" ),
    path('service_home', views.service_home, name ="service_home" ),
    path('owner_home/items', views.items, name ="items" ),
]
