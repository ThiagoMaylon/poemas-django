from django.urls import path
from .views import my_login, cadastro

urlpatterns = [
    path('login/', my_login, name='login'),
    path('cadastro/', cadastro, name='cadastro'),
]