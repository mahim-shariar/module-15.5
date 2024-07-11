from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from . import forms
from .models import Album
from django.views.generic import CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
# Create your views here.

# Create your views here.

@method_decorator(login_required, name='dispatch')
class AddAlbumView(CreateView):
    form_class = forms.AlbumForm
    model = Album
    template_name = 'add_albums.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

@method_decorator(login_required, name='dispatch')
class edit_album(UpdateView):
    model = Album
    form_class = forms.AlbumForm
    template_name = "add_albums.html"
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('home')

@method_decorator(login_required, name='dispatch')
class delete_album(DeleteView):
    model = Album
    template_name = "delete.html"
    success_url = reverse_lazy('home')
    pk_url_kwarg = 'id'
