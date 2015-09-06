from django.db import models

# Create your models here.


class Artist(models.Model):
    name = models.CharField('artist name', max_length=50)
    country = models.CharField(max_length=50)
    beginning = models.DateField('carier start')
    end = models.CharField('carier end', max_length=50)
    biography = models.TextField(blank=True)
    photo = models.ImageField(upload_to='photo/%Y')
    artist_rate = models.IntegerField(default=0)
    date_create = models.DateField(auto_now=True)

    def __str__(self):
        return self.name


class Album(models.Model):
    artist = models.ForeignKey(Artist)
    title = models.CharField(max_length=50)
    describe = models.TextField('album description', blank=True)
    release_date = models.DateField()
    image = models.ImageField(upload_to='images/%Y')
    album_rate = models.IntegerField(default=0)
    date_add = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
