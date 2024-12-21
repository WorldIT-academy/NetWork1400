from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.db.utils import IntegrityError
from django.contrib.auth import authenticate, login


def render_registration(request):
    context = {}
    if request.method == 'POST':
        print(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')
        if password == password_confirm:
            try:
                User.objects.create_user(username= username, password= password)
                return redirect('login')
            except IntegrityError:
                context = {'same_user' : True}
        else:
            context = {'same_password' : False}
    return render(request=request, template_name= "user_app/registration.html", context=context)


def render_login(request):
    context = {}
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request = request,username = username, password = password)
        if user:
            login(request = request, user = user)
        else:
            context = {"error" : True}
    return render(request=request, template_name='user_app/login.html', context=context)