from django.urls import path
from .views import *


urlpatterns = [
    path('all_posts/', render_all_posts)
]