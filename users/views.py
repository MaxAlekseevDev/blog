from django.shortcuts import render

from django_registration.backends.activation.views import RegistrationView

# Create your views here.
class RegisterUser(RegistrationView):
    template_name = 'registration_form'

    def create_inactive_user(self):
        pass
    