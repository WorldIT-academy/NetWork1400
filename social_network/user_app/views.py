from django.shortcuts import render
from django.contrib.auth.models import User


def render_registration(request):
    if request.method == 'POST':
        print(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        User.objects.create_user(username= username, password= password)
    return render(request=request, template_name= "user_app/registration.html")


