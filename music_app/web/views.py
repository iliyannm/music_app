from django.shortcuts import render, redirect

from music_app.web.forms import CreateProfileForm, DeleteProfileForm, CreateAlbumForm, EditAlbumForm, DeleteAlbumForm
from music_app.web.models import Profile, Album


def get_profile():
    profiles = Profile.objects.all()
    if profiles:
        return profiles[0]
    return None


# DONE
def show_index(request):
    profile = get_profile()
    albums = Album.objects.all()

    context = {
        'profile': profile,
        'albums': albums,
    }

    if profile:
        return render(request, 'home-with-profile.html', context)

    return redirect('create profile')


# DONE
def create_album(request):
    profile = get_profile()
    if request.method == 'POST':
        form = CreateAlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show index')
    else:
        form = CreateAlbumForm()

    context = {
        'form': form,
        'profile': profile,
    }
    return render(request, 'add-album.html', context)


# DONE
def show_album_details(request, pk):
    profile = get_profile()
    album = Album.objects.get(pk=pk)

    context = {
        'profile': profile,
        'album': album,
    }

    return render(request, 'album-details.html', context)


# DONE
def edit_album(request, pk):
    profile = get_profile()
    album = Album.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditAlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('show index')
    else:
        form = EditAlbumForm(instance=album)

    context = {
        'form': form,
        'album': album,
        'profile': profile,
    }

    return render(request, 'edit-album.html', context)


# DONE
def delete_album(request, pk):
    profile = get_profile()
    album = Album.objects.get(pk=pk)
    if request.method == 'POST':
        form = DeleteAlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('show index')
    else:
        form = DeleteAlbumForm(instance=album)

    context = {
        'form': form,
        'album': album,
        'profile': profile,
    }

    return render(request, 'delete-album.html', context)


# DONE
def show_profile_details(request):
    profile = get_profile()
    albums = Album.objects.all()
    albums_count = len(albums)

    context = {
        'profile': profile,
        'albums_count': albums_count,
    }

    return render(request, 'profile-details.html', context)


# DONE
def delete_profile(request):
    profile = get_profile()
    if request.method == "POST":
        form = DeleteProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('show index')
    else:
        form = DeleteProfileForm(instance=profile)

    context = {
        'form': form,
        'profile': profile,
    }

    return render(request, 'profile-delete.html', context)


# DONE
def create_profile(request):
    profile = get_profile()
    if request.method == "POST":
        form = CreateProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('show index')
    else:
        form = CreateProfileForm()

    context = {
        'form': form,
        'profile': profile,
    }

    return render(request, 'home-no-profile.html', context)

