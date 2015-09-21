from django.contrib import admin
from .models import *
# Register your models here.


class AlbumInline(admin.TabularInline):
    model = Album
    extra = 1


class CommentsInline(admin.TabularInline):
    model = Comments
    extra = 5


class AlbumAdmin(admin.TabularInline):
    inlines = [CommentsInline]


class ArtistAdmin(admin.ModelAdmin):
    inlines = [AlbumInline]
    search_fields = ('name', 'country')
    fieldsets = [
        ('Artist Information', {'fields': ['name', 'country', 'beginning', 'end', 'photo']}),
        ('Description', {'fields': ['biography'], 'classes': ['collapse']}),
        (None, {'fields': ['artist_rate']}),
    ]
    list_display = ('name', 'country', 'artist_rate')

admin.site.register(Artist, ArtistAdmin)
# admin.site.register(Album, AlbumAdmin)
admin.site.register(Comments)

