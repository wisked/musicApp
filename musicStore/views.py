from django.shortcuts import render
from .models import *
# Create your views here.


def index(request):
    artists = Artist.objects.all()
    return render(request, 'musicStore/index.html', {'artists': artists})