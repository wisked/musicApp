from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import staticfiles
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^albums/$', views.allAlbums, name='allAlbums'),
    # url(r'searching/(?P<l>\W+)^$', views.searching, name='searching'),
    url(r'^artist/(?P<pk>[0-9]+)/$', views.artistInformation, name='artistInformation'),
    url(r'^artist/[0-9]+/album/(?P<pk>[0-9]+)/$', views.albumDetails, name='albumDetails'),
    url(r'^artist/[0-9]+/album/(?P<pk>[0-9]+)/addlikes/$', views.addLike, name='addLike'),
    url(r'^artist/[0-9]+/album/(?P<pk>[0-9]+)/addcomment/$', views.addComment, name='addComment'),
    url(r'^page/(\d+)/$', views.allAlbums, name='allAlbums'),
    url(r'searching/(?P<st>\w+)^$', views.searching, name='searching'),
    # url(r'^artist/[0-9]+/album/(?P<pk>[0-9]+)/comments/$', views.comments, name='comments'),
 ]



# urlpatterns += staticfiles_urlpatterns()
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)