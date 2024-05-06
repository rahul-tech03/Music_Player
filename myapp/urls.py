from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from .views import add_to_listen_later
urlpatterns = [
    path('',views.index, name='index'),
    path('soor/',views.soor, name='soor'),
    path('song/', views.song, name='song'),
    path('song/<int:id>', views.play, name='play'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout', views.logout, name='logout'),
    path('hindisongs/', views.hindisongs, name='hindisongs'),
    path('englishsongs/', views.englishsongs, name='englishsongs'),
    path('listenlater/', views.listen_later_list, name='ll'),
    path('add_to_listen_later/<int:song_id>/', add_to_listen_later, name='add_to_listen_later'),
    path('remove_from_listen_later/<int:song_id>/', views.remove_from_listen_later, name='remove_from_listen_later'),
    path('favorites/', views.favorite_list, name='favorite'),
    path('add_to_favorite/<int:song_id>/', views.add_to_favorite, name='add_to_favorite'),
    path('remove_from_favorite/<int:song_id>/', views.remove_from_favorite, name='remove_from_favorite'),
    path('playlist/', views.playlist, name='playlist'),
    path('add_to_playlist/<int:song_id>/', views.add_to_playlist, name='add_to_playlist'),
    path('remove_from_playlist/<int:song_id>/', views.remove_from_playlist, name='remove_from_playlist'),
    path('search/', views.search, name='search'),


] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

