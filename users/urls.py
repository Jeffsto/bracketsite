from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.members, name='users'),
    path('users/details/<int:id>',views.details, name='details'),
    path('',views.main,name='main')
    path('testing',views.testing,name='testing')
]
