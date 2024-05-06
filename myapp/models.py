from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Song(models.Model):
    
    song_id = models.AutoField(primary_key=True)
    song_name=models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    language = models.CharField(max_length=20,default='Hindi')
    tags = models.CharField(max_length=100)
    image = models.ImageField(upload_to='docs')
    song = models.FileField(upload_to='docs')
   
    def __str__(self):
        return self.song_name
   


class ListenLater(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} - {self.song.song_name}"


# todays code 16
    
class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} - {self.song.song_name}"
    

   
class Playlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} - {self.song.song_name}"