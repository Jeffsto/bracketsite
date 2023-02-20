from django.urls import path
from . import views

urlpatterns = [
    path('',views.main,name='main'),
    path('login_user', views.login_user, name='login'),
]
