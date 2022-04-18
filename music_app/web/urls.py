from django.urls import path

from music_app.web.views import show_index, create_album, show_album_details, edit_album, delete_album, \
    show_profile_details, delete_profile, create_profile

urlpatterns = (
    path('', show_index, name='show index'),
    path('album/add/', create_album, name='create album'),
    path('album/details/<int:pk>/', show_album_details, name='show album details'),
    path('album/edit/<int:pk>/', edit_album, name='edit album'),
    path('album/delete/<int:pk>/', delete_album, name='delete album'),
    path('profile/details/', show_profile_details, name='show profile details'),
    path('profile/delete/', delete_profile, name= 'delete profile'),
    path('profile/create/', create_profile, name='create profile'),
)
