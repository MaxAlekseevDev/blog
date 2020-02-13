from django.contrib import admin
from django.urls import path, include


from Posts.views import hello

api_name = 'posts'

urlpatterns = [
    path('', hello, name='index'),
]


