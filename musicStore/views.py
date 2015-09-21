from django.shortcuts import render, get_object_or_404, Http404, redirect, render_to_response
from django.views import generic
from .models import *
from .forms import *
from django.core.context_processors import csrf
from django.contrib import auth
# Create your views here.


# def index(request):
#     artists = Artist.objects.order_by('date_create')[:10]
#     return render(request, 'musicStore/index.html', {'artists': artists})
# def base(request):
#     artists = Artist.objects.all()
#     render_to_response('base.html', artists)

class IndexView(generic.ListView):
    template_name = 'musicStore/index.html'
    context_object_name = 'artists'

    def get_queryset(self):
        return Artist.objects.order_by('date_create')[:10]


def searching(request, l):
    args = {}
    args['artists'] = Artist.objects.filter(name__startswith=l)
    return render_to_response('musicStore/searching.html', args)


def artistInformation(request, pk):
    artist = get_object_or_404(Artist, id=pk)
    albums = Album.objects.filter(artist_id=pk)
    username = auth.get_user(request).username
    return render(request, 'musicStore/artistInformation.html', {'artist': artist, 'albums': albums, 'username': username})


def allAlbums(request):
    albums = Album.objects.all()
    return render_to_response('musicStore/allAlbums.html', {'albums': albums, 'username': auth.get_user(request).username})


# def albumDetails(request, pk):
#     album = get_object_or_404(Album, id=pk)
#     album_comments = Comments.objects.filter(album_id=pk)
#     return render(request, 'musicStore/albumDetails.html', {'album': album, 'album_comments': album_comments})


def comments(request, pk):
    comment = Comments.objects.filter(id=pk)
    return render(request, 'musicStore/comments.html', {'comment': comment})


def albumDetails(request, pk):
    comment_form = CommentForm
    args = {}
    args.update(csrf(request))
    args['album'] = Album.objects.get(id=pk)
    args['album_comments'] = Comments.objects.filter(album_id=pk)
    args['form'] = comment_form
    args['username'] = auth.get_user(request).username
    return render_to_response('musicStore/albumDetails.html', args)


def addLike(request, pk):
    if 'likePause' not in request.session:
        album = get_object_or_404(Album, id=pk)
        album.user_rate += 1
        album.save()
        request.session.set_expiry(120)
        request.session['likePause'] = True
        # response = redirect('/')
        # response.set_cookie(1, 'twst')
        return redirect('/musicstore/artist/%s/album/%s' % (album.artist_id, album.id))
    else:
        album = get_object_or_404(Album, id=pk)
    return redirect('/musicstore/artist/%s/album/%s' % (album.artist_id, album.id))


def addComment(request, pk):
    if request.POST and ('pause' not in request.session):
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.album = Album.objects.get(id=pk)
            form.save()
            request.session.set_expiry(60)
            request.session['pause'] = True
    return redirect('/musicstore/artist/%s/album/%s/' % (Album.objects.get(id=pk).artist_id, pk))