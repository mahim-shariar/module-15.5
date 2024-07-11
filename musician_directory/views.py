from django.shortcuts import render, redirect
from . import forms
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy
from .models import muisician
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
# Create your views here.

@method_decorator(login_required, name='dispatch')
class add_musician(CreateView):
    model = muisician
    form_class =forms.MusicianForm
    template_name = "add_musician.html"
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
# @method_decorator(login_required, name='dispatch')
class edit_musician(UpdateView):
    model = muisician
    form_class =forms.MusicianForm
    template_name = "edit_musician.html"
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('home')

