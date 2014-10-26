from django.shortcuts import render, get_object_or_404
from django.core.files import File
from django.views.generic.base import View
import json

class UploadView(View):

    def post(self, request, *args, **kwargs):
        print ('post')
        print (request.FILES)
        print (request.POST)
        
        movie = MovieToGuess()
        movie.movie = request.FILES['movie']
        movie.userId = request.POST['userid']
        movie.name = request.POST['name']
        movie.question = request.POST['question']
        movie.guessSecond = request.POST['second']
        movie.guessA = request.POST['guessA']
        movie.guessB = request.POST['guessB']
        
        for hashtag in json.loads(reqest.POST['hashtags']):
            hashtagObject = None
            try:
                Hashtag.objects.get(tag=hashtag)
            except DoesNotExist:
                hashtagObject = HashTag(tag = hashtag)
                hashtagObject.save()
            movie.hashtags.add(hashtagObject)
        
        movie.save()
