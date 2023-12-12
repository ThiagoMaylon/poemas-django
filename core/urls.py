from django.urls import path, include
from .views import index, post

urlpatterns = [
    path('', index, name='index'),
    path('post/', post, name='post'),
]