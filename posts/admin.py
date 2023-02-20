from django.contrib import admin
from .models import Post, Hashtag
# Register your models here.

admin.site.register(Hashtag)
admin.site.register(Post)