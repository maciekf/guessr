from django.shortcuts import render, get_object_or_404
from django.core.files import File
from django.views.generic.base import View
from django.http import HttpResponse
from .models import *
import json

class UploadView(View):
    def post(self, request, *args, **kwargs):
        print ('post')
        print (request.FILES)
        
        movie = MovieToGuess()
        movie.movie = request.FILES['movie']
        movie.userId = request.POST['userid']
        movie.name = request.POST['name']
        movie.question = request.POST['question']
        movie.guessSecond = request.POST['second']
        movie.guessA = request.POST['guessA']
        movie.guessB = request.POST['guessB']
        
        for hashtag in json.loads(request.POST['hashtags']):
            hashtagObject = None
            try:
                Hashtag.objects.get(tag=hashtag)
            except DoesNotExist:
                hashtagObject = HashTag(tag = hashtag)
                hashtagObject.save()
            movie.hashtags.add(hashtagObject)
        
        print (request.POST['userid'])
        
        movie.save()

        return HttpResponse(
            json.dumps({'status' : 1}),
            content_type="application/json"
        )        
        

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
