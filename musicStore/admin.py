from django.contrib import admin
from .models import *
# Register your models here.


class AlbumInline(admin.TabularInline):
    model = Album
    extra = 1


class ArtistAdmin(admin.ModelAdmin):
    inlines = [AlbumInline]
    search_fields = ('name', 'country')
    fieldsets = [
        ('Artist Information', {'fields': ['name', 'country', 'beginning', 'end', 'photo']}),
        ('Description', {'fields': ['biography'], 'classes': ['collapse']}),
        (None, {'fields': ['artist_rate']}),
    ]
    list_display = ('name', 'country')

admin.site.register(Artist, ArtistAdmin)


