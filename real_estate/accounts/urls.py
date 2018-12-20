from django.urls import path
from .views import *

urlpatterns = [
    path('register/', register, name='register'),
    path('logout/', user_logout, name='logout'),
    path('login/', user_login, name='login'),
    path('dashboard/', dashboard, name='dashboard'),
]