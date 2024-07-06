
from django.shortcuts import render, redirect, get_object_or_404
from . import forms
from .models import Album

# Create your views here.

# Create your views here.
def add_album(request):
    if request.method == 'POST':
        album_form = forms.AlbumForm(request.POST)
        if album_form.is_valid():
            album_form.save()
            return redirect('add_albums')
    else:
        album_form = forms.AlbumForm(request.POST)
    return render(request,'add_albums.html',{'form':album_form})



def edit_album(request,id):
    album = Album.objects.get(pk=id)
    album_form = forms.AlbumForm(instance=album)
    if request.method == 'POST':
        album_form = forms.AlbumForm(request.POST,instance=album)
        if album_form.is_valid():
            album_form.save()
            return redirect('home')
    return render(request,'add_albums.html',{'form':album_form})


def delete_album(request,id):
    post = Album.objects.get(pk=id)
    post.delete()
    return redirect('home')