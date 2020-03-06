from django.urls import path, include

from .views import RegisterUser

app_name = 'users'

urlpatterns = [
    path('', include('django_registration.backends.activation.urls')),
    
]