from django.urls import path, include

from . import views

urlpatterns = [

    path('add_albums/', views.AddAlbumView.as_view(), name='add_albums'),
    path('edit/<int:id>/', views.edit_album.as_view(), name='edit_album'),
    path('delete/<int:id>/', views.delete_album.as_view(), name='delete_album'),
]
