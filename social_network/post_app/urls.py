from django.urls import path
from .views import *


urlpatterns = [
    path('all_posts/', render_all_posts, name = 'all_posts'),
    path('create_post/', render_create_post),
]
