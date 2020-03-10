from django.shortcuts import render
from django.contrib.auth import logout
from django.contrib.auth.models import User

from django_registration.backends.activation.views import RegistrationView
from django_registration.forms import RegistrationForm
class RegisterUser(RegistrationView):
    template_name = 'registration_form'
    form_class = RegistrationForm

def logout_view(request):
    logout(request)
    return render(request, 'registration/logout.html')
        
        
    