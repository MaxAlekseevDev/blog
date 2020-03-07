from django.urls import path, include
from django.contrib.auth import views as auth_views

from .views import RegisterUser

app_name = 'users'

urlpatterns = [
    path('', include('django_registration.backends.one_step.urls')),
    path('', include('django.contrib.auth.urls')),
    
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout')
    
]