from django.db import models
from django.core.files import File

# Create your models here.

class HashTag(models.Model):
    tag = models.CharField(max_length=40)

    def __str__(self):
        return self.tag

class MovieToGuess(models.Model):
    userId = models.IntegerField()
    name = models.CharField(max_length=100)
    minature = models.FileField(upload_to = 'minatures', null = True)
    movie = models.FileField(upload_to = 'movies', null = True)
    stopTime = models.CharField(max_length=20)
    question = models.CharField(max_length=300)
    goodAnswer = models.CharField(max_length=300)
    wrongAnswer = models.CharField(max_length=300)
    hashtags = models.ManyToManyField(HashTag)

    def __str__(self):
        return self.name
