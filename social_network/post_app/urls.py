from django.urls import path
from .views import *


urlpatterns = [
    path('all_posts/', render_all_posts, name = 'all_posts'),
    path('create_post/', render_create_post),
    path('create_tag/', render_create_tag, name= 'create_tag'),
    path('all_tags/', render_all_tags, name='all_tags')
]
