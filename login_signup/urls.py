
from django.contrib import admin
from django.urls import path
from login_signup import views
#from shop_owner import views
import pymongo 


urlpatterns = [
    path('', views.login, name = "login"),
]
