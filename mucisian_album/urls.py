
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home, name='home'),
    path('album/', include('albums.urls')),
    path('musician/', include('musician_directory.urls')),
    path('user/', include('User_auth.urls')),
]
