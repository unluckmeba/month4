from django.contrib import admin
from django.urls import path
from posts.views import main_page_view, posts_view, hashtags_view, post_detail_view
from django.conf.urls.static import static
from Blog.settings import MEDIA_URL, MEDIA_ROOT

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_page_view),
    path('posts/', posts_view),
    path('posts/<int:id>/', post_detail_view),
    path('hashtags/', hashtags_view)
]

urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
