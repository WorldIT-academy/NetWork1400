from django.shortcuts import render, redirect
from .models import Post, Tag
from django.core.files.storage import FileSystemStorage
from user_app.models import Profile
import os
from django.contrib.auth.decorators import login_required
from .forms import PostForm


def render_all_posts(request):
    all_posts = Post.objects.all()
    return render(request,"post_app/all_posts.html",context={"all_posts":all_posts})   

# Декоратор перевіряє, чи залогінився користувач,
# Якщо ні - його перекидає на сторінку логіну, шлях до йкої прописано у констатні LOGIN_URL у settings.py
@login_required
def render_create_post(request):
    # Якщо надсилається тип запиту POST, тобто користувач надсилає форму
    if request.method == "POST":
        # Створюємо об'єкт форми та наповнюємо її даними та файлами, які надсилають користувачі через форму
        form = PostForm(request.POST, request.FILES)
        # Якщо надіслані дані є коректними (якщо пройшла валідація)
        if form.is_valid():
            post = Post.objects.create(
                title = form.cleaned_data.get('title'),
                content = form.cleaned_data.get('content'),
                image = form.cleaned_data.get('image'),
                author = Profile.objects.get(user= request.user)
            )
            post.tags.set(form.cleaned_data.get('tags'))
            post.save()

            return redirect('all_posts')
    else:
        # Створюємо порожню форму для відображення на сторінці
        form = PostForm()
        
    return render(request, "post_app/create_post.html", context={'form': form})