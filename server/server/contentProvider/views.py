from django.shortcuts import render
from django.http import HttpResponse
from models import MovieToGuess
import json

# Create your views here.

def tagged_videos(request, tag=None):
    tagged_vids = MovieToGuess.objects.filter(hashtags__tag=tag)
    urls = [
        {'id': tagged.id, 'miniature': tagged.miniature, 'name': tagged.name}
        for tagged in tagged_vids
    ]
    return HttpResponse(
        json.dumps({'videos' : urls}),
        content_type="application/json"
    )


def get_video(request, video_id=None):
    video = MovieToGuess.objects.get(id=video_id)
    result = {
        'video' : video.movie,
        'question': video.question,
        'goodAnswer': video.goodAnswer,
        'wrongAnswer': video.badAnswer,
        'stopTime': video.stopTime
    }
    return HttpResponse(
        json.dumps(result),
        content_type="application/json"
    )