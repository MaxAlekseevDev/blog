from django.urls import path, include
from django.contrib.auth import views as auth_views

from users.views import logout_view

app_name = 'users'

urlpatterns = [
    path('', include('django_registration.backends.one_step.urls')),
        
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout')
    
]