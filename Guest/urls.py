from django.contrib import admin
from django.urls import path
from Guest import views
app_name="Guest"

urlpatterns = [
    path("UserRegistration/",views.UserRegistration,name="UserRegistration"),
    path("Login/",views.Login,name="Login"),
    path("",views.index,name="index"),
]