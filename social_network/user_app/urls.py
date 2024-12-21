from django.urls import path
from .views import *


urlpatterns = [
    path('registration/', render_registration),
    path('login/', render_login, name= 'login')
]