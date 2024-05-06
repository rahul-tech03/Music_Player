from .models import Song
from django.shortcuts import render
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.views import LogoutView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.shortcuts import redirect
from django.contrib.auth import logout as auth_logout
from .models import *
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import ListenLater, Song, Favorite, Playlist


@login_required
def add_to_listen_later(request, song_id):
    user = request.user
    song = get_object_or_404(Song, pk=song_id)

    if not ListenLater.objects.filter(user=user, song=song).exists():
        ListenLater.objects.create(user=user, song=song)
    return redirect('/listenlater/')


@login_required
def listen_later_list(request):
    user = request.user
    song_list = ListenLater.objects.filter(user=user)
    return render(request, 'listen_later.html', {'song_list': song_list})


def index(request):
    song = Song.objects.all()
    query = request.GET.get('query')
    if query:
        song_results = Song.objects.filter(song_name__icontains=query)
    else:
        song_results = None
    return render(request, 'soor.html', {'song': song, 'song_results': song_results})


def soor(request):
    song = Song.objects.all()
    return render(request, 'soor.html', {'song': song})


def song(request):
    song = Song.objects.all()
    return render(request, 'song.html', {'song': song})


def hindisongs(request):
    song = Song.objects.all()
    return render(request, 'hindisongs.html', {'song': song})


def englishsongs(request):
    song = Song.objects.all()
    return render(request, 'englishsongs.html', {'song': song})


def play(request, id):
    song = Song.objects.filter(song_id=id).first()
    return render(request, 'playpage.html', {'song': song})


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        from django.contrib.auth import login
        login(request, user)
        return redirect('/')
    return render(request, 'login.html')


def signup(request):
    if request.method == "POST":
        email = request.POST['email']
        username = request.POST['username']
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        password = request.POST['password']
        password2 = request.POST['password2']

        myuser = User.objects.create_user(username, email, password)
        myuser.first_name = first_name
        myuser.last_name = last_name
        myuser.save()
        user = authenticate(username=username, password=password)
        from django.contrib.auth import login
        login(request, user)

        return redirect('/')
    return render(request, 'signup.html')


def logout(request):
    auth_logout(request)
    return redirect('/')


def remove_from_listen_later(request, song_id):
    song = get_object_or_404(Song, pk=song_id)
    ListenLater.objects.filter(user=request.user, song=song).delete()
    return redirect('/')


# todays code16

@login_required
def add_to_favorite(request, song_id):
    user = request.user
    song = get_object_or_404(Song, pk=song_id)

    # Check if the song is already in the user's "Listen Later" list
    if not Favorite.objects.filter(user=user, song=song).exists():
        Favorite.objects.create(user=user, song=song)
    return redirect('/favorites/')


@login_required
def favorite_list(request):
    user = request.user
    song_list = Favorite.objects.filter(user=user)
    return render(request, 'favorite.html', {'song_list': song_list})


def remove_from_favorite(request, song_id):
    song = get_object_or_404(Song, pk=song_id)
    Favorite.objects.filter(user=request.user, song=song).delete()
    return redirect('/')





@login_required
def add_to_playlist(request, song_id):
    user = request.user
    song = get_object_or_404(Song, pk=song_id)

    # Check if the song is already in the user's "Listen Later" list
    if not Playlist.objects.filter(user=user, song=song).exists():
        Playlist.objects.create(user=user, song=song)
    return redirect('/playlist/')


@login_required
def playlist(request):
    user = request.user
    song_list = Playlist.objects.filter(user=user)
    return render(request, 'playlist.html', {'song_list': song_list})


def remove_from_playlist(request, song_id):
    song = get_object_or_404(Song, pk=song_id)
    Playlist.objects.filter(user=request.user, song=song).delete()
    return redirect('/')



def search(request):
    query = request.GET.get('query')

    if query:
        song_results = Song.objects.filter(song_name__icontains=query)
    else:
        song_results = Song.objects.all()
    return render(request, 'search.html', {'song_results': song_results})
