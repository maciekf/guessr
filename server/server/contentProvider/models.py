from django.db import models
from django.core.files import File
import cv2

# Create your models here.

class HashTag(models.Model):
    tag = models.CharField(max_length=40)

    def __str__(self):
        return self.tag

class MovieToGuess(models.Model):
    userId = models.IntegerField()

    name = models.CharField(max_length=100)
    minature = models.FileField(upload_to = 'minatures')

    movie = models.FileField(upload_to = 'movies')
    ending = models.FileField(upload_to = 'movies')

    guessA = models.CharField(max_length=300)
    guessB = models.CharField(max_length=300)

    hashtags = models.ManyToManyField(HashTag)

    def create_miniature(self):
        assert self.movie
        cap = cv2.VideoCapture(self.movie)
        _, image = cap.read()
        self.minature.save(self.minature.url, File(image))

    def __str__(self):
        return self.name
