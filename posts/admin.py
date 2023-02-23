from django.contrib import admin
from .models import Post, Hashtag, Comment
# Register your models here.

admin.site.register(Hashtag)
admin.site.register(Post)
admin.site.register(Comment)
