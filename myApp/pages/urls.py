from django.urls import path
from . import views

urlpatterns=[
    path ('index',views.index,name='index'),
    path ('login',views.login,name='login'),
    path('register' ,views.register,name='register'),
    path('dash' ,views.dash,name='dash'),
]