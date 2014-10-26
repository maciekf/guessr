import requests
import json

url = 'http://127.0.0.1:8000/upload'

files = {'movie': open('cos.mov', 'rb')}
data = {'userid' : 1, 'name' : 'kupacz', 'question' : 'co jest?',
    'stopTime' : '2', 'goodAnswer' : 'A', 'badAnswer' : 'B', 'hashtags' : '[]'}

def go_gg():
    requests.post(url, files=files, data=data)
