from django.shortcuts import render, redirect
from .models import Post, Tag
from user_app.models import Profile
from django.contrib.auth.decorators import login_required   
from .forms import PostForm, TagForm
from django.contrib.admin.views.decorators import staff_member_required


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
            # Отримуємо автора на основі авторизованого користувача
            author = Profile.objects.get(user = request.user)
            # Збергаіємо форму БД
            form.save(author)
            return redirect('all_posts')
    else:
        # Створюємо порожню форму для відображення на сторінці
        form = PostForm()
        
    return render(request, "post_app/create_post.html", context={'form': form})

@staff_member_required
def render_create_tag(request):
    # Якщо надсилається тип запиту POST, тобто користувач надсилає форму
    if request.method == "POST":
        # Створюємо об'єкт форми та наповнюємо її даними та файлами, які надсилають користувачі через форму
        form = TagForm(request.POST, request.FILES)
        # Якщо надіслані дані є коректними (якщо пройшла валідація)
        if form.is_valid():
            # Збергаіємо форму БД
            form.save()
            return redirect('all_tags')
    else:
        # Створюємо порожню форму для відображення на сторінці
        form = TagForm()
        
    return render(request, "post_app/create_tag.html", context={'form': form})

def render_all_tags(request):
    tags = Tag.objects.filter(active = True)
    context = {"tags": tags}
    return render(request=request, template_name= 'post_app/all_tags.html', context=context)
    