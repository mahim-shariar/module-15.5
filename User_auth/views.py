from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# from posts.models import Post
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from .forms import RegistrationForm
from django.contrib.auth.models import User


# Create your views here.


class RegisterView(FormView):

    form_class = RegistrationForm
    success_url = reverse_lazy('home')
    template_name = 'register.html'

    def form_valid(self, form):
        user = form.save()
        messages.success(self.request, 'Loged in Successfully')
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return super().form_valid(form)


class UserLoginView(LoginView):
    template_name = 'register.html'

    def get_success_url(self):
        return reverse_lazy('home')

    def form_valid(self, form):
        messages.success(self.request, 'Loged in Successfully')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.success(self.request, 'Loged in information Incorrect')
        return super().form_invalid(form)


class UserLogoutView(LogoutView):
    next_page = reverse_lazy('home')
