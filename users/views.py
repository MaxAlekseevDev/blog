from django.shortcuts import render

from django_registration.backends.activation.views import RegistrationView
from django_registration.forms import RegistrationForm
class RegisterUser(RegistrationView):
    template_name = 'registration_form'
    form_class = RegistrationForm

    

        
        
    