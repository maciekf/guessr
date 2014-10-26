from django.shortcuts import render
from django.http import HttpResponse
from models import MovieToGuess
import json

# Create your views here.

def tagged_videos(request, tag=None):
    tagged_vids = MovieToGuess.objects.filter(hashtags__tag=tag)
    urls = [
        {'id': tagged.id, 'url': tagged.miniature, 'name': tagged.name}
        for tagged in tagged_vids
    ]
    return HttpResponse(
        json.dumps({'videos' : urls}),
        content_type="application/json"
    )
