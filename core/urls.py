from django.urls import path
from .views import index, post

urlpatterns = [
    path('', index, name='index'),
    path('post/', post, name='post'),
]