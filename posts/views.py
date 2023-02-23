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


def main_page_view(request):
    if request.method == 'GET':
        return render(request, 'layouts/main.html')


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


def post_detail_view(request, id):
    if request.method == 'GET':
        post = Post.objects.get(id=id)

        context = {
            'post': post
        }

        return render(request, 'posts/post_detail.html', context=context)


class PostDetailView(DetailView, CreateView):
    template_name = 'posts/post_detail.html'
    queryset = Post.objects.all()
    pk_url_kwarg = 'id'

    def get_context_data(self, **kwargs):
        return {
            'post': self.get_object(),
            'comments': Comment.objects.filter(post=self.get_object())
        }
