from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.members, name='users'),
    path('users/details/<int:id>',views.details, name='details'),
    path('users/testing',views.testing,name='testing'),
]
