from django.shortcuts import render

# Create your views here.
from django.shortcuts import redirect, HttpResponse
from datetime import date
from django.views.generic import ListView, DetailView, CreateView
from posts.models import *


# Create your views here.

def hello_view(request):
    if request.method == 'GET':
        return HttpResponse('Hello! its my project')


def now_date_view(request):
    if request.method == 'GET':
        return HttpResponse(f'Now date: {date.today()}')


def hashtags_view(request):
    if request.method == 'GET':
        data = {
            'hashtags': Hashtag.objects.all()
        }
        return render(request, 'posts/hashtags.html', context=data)


def posts_view(request):
    if request.method == 'GET':
        data = {
            'posts': Post.objects.all()
        }
        return render(request, 'posts/posts.html', context=data)
