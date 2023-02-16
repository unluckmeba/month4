from django.shortcuts import render

# Create your views here.
from django.shortcuts import redirect, HttpResponse
from datetime import date


# Create your views here.

def hello_view(request):
    if request.method == 'GET':
        return HttpResponse('Hello! its my project')


def now_date_view(request):
    if request.method == 'GET':
        return HttpResponse(f'Now date: {date.today()}')


def goodbye_view(request):
    if request.method == 'GET':
        return HttpResponse('Goodbye user!')
