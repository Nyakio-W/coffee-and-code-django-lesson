from django.shortcuts import render
import requests 

def home(request):
  response = requests.get('https://api.github.com/events')
  data = response.json() 
  result = data [0]['repo']
  return render(request, 'templates/index.html',{'result':result})