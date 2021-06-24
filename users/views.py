from django.shortcuts import render

# my imports
from django.urls import reverse_lazy
from users.forms import CustomUserCreationForm
from django.views.generic import CreateView


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
