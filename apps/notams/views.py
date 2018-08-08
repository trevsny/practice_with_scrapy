from django.shortcuts import render, HttpResponse, redirect
# import urllib3
# import json
import importlib
import scrapy
from .models import * 
# usana = input('ourfirstscraper:')
importlib.import_module('ourfirstscraper')
# Create your views here.

def index(request):
    # response = "Hello, I am your first request!"
    # return HttpResponse(response)
    context = {
        'notams':Notam.objects.all()
    }
    return render(request,'notams/index.html', context)

def api(request):
    # call api
    ##response = urllib2.urlopen('https://v4p4sz5ijk.execute-api.us-east-1.amazonaws.com/anbdata/states/notams/notams-realtime-list?api_key=34b8ea10-9138-11e8-9b27-2b57524d59b4&state=USA&format=json&locations=ksfo')
    ##data = json.load(response)
    # loop through data variable and only print Notams
    # for notam in data
    #     print notam.all

    return redirect('/')

def create(request):
    # Add Notam to list of notams pilot wants to refer to
    newNotam = Notam.objects.create(description = request.POST['description'])
    return redirect('/')

def find(request):
    
    return render(request,'notams/concert.html')