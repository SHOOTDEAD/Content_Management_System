from django.urls import path
from .views import *


urlpatterns = [
    path("",home_page,name="home"),
    path("login",login,name="login"),
    path("signup",signup,name='signup'),
    path("logout",logout,name='logout'),
]
