from django.shortcuts import render

from django.http import HttpResponse

from datetime import datetime


from lectures.models import Lecture

# Create your views here.

def welcome(request):
    return render(request, 'website/home.html', {"lectures": Lecture.objects.all()})

def date(request):
    return HttpResponse(f'This page was served at {str(datetime.now())}')

def about(request):
    return HttpResponse("It is about anatomy lectures holding in different venue.")  

