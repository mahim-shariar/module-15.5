from django.urls import path, include

from . import views

urlpatterns = [

    path('add_albums/', views.add_album, name='add_albums'),
    path('edit/<int:id>/', views.edit_album, name='edit_album'),
    path('delete/<int:id>/', views.delete_album, name='delete_album'),
]
