import requests
import json

url = 'http://127.0.0.1:8000/'

files = {'movie': open('cos.mov', 'rb')}
data = {'userid' : 1, 'name' : 'kupacz', 'question' : 'co jest?',
    'second' : '2', 'guessA' : 'A', 'guessB' : 'B', 'hashtags' : '[]'}

def go_gg():
    requests.post(url, files=files, data=data)
