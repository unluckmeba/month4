from django.shortcuts import render

# Create your views here.
from django.shortcuts import redirect, HttpResponse
from datetime import date
from django.views.generic import DetailView, CreateView
from posts.forms import PostCreateForm, CommentCreateForm
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
            'post': post,
            'comments': post.commets.all(),
            'form': CommentCreateForm
        }

        return render(request, 'posts/post_detail.html', context=context)

    if request.method == 'POST':
        post = Post.objects.get(id=id)
        data = request.POST
        form = CommentCreateForm(data=data)

        if form.is_valid():
            Comment.objects.create(
                text=form.cleaned_data.get('text'),
                post=post
            )

        context = {
            'post': post,
            'comment': post.comments.all(),
            'form': form
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


def create_post_view(request):
    if request.method == 'GET':
        context = {
            'form': PostCreateForm
        }
        return render(request, 'posts/create.html', context=context)

    if request.method == 'POST':
        data, files = request.POST, request.FILES

        form = PostCreateForm(data, files)

        if form.is_valid():
            Post.objects.create(
                image=form.cleaned_data.get('image'),
                tittle=form.cleaned_data.get('tittle'),
                description=form.cleaned_data.get('description'),
                rate=form.cleaned_data.get('rate')
            )
            return redirect('/posts')

        return render(request, 'posts/create.html', context={
            'form': form
        })
