from django.shortcuts  import render,redirect
from albums.models import Album
def home(request):
    data = Album.objects.all()
    return render(request,'home.html',{'data':data})