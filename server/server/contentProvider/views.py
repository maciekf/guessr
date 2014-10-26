from django.shortcuts import render
from django.http import HttpResponse
from models import MovieToGuess
import json

# Create your views here.

def tagged_videos(request, tag=None):
    tagged_vids = MovieToGuess.objects.filter(tags__name=tag)
    urls = [tagged.url for tagged in tagged_vids]
    return HttpResponse(
        json.dumps({'videos' : urls}),
        content_type="application/json"
    )
