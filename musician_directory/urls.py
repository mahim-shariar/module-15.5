from django.urls import path, include

from . import views

urlpatterns = [
    
    path('add_musician/', views.add_musician, name='add_musician'),
]
