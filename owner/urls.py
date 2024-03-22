from django.contrib import admin
from django.urls import path
from login_signup import views
from owner import views 


urlpatterns = [
    path('owner_home', views.owner_home, name ="owner_home" ),
    path('service_home', views.service_home, name ="service_home" ),
]