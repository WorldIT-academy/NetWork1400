from django.shortcuts import render
from .models import Post, Tag
from django.core.files.storage import FileSystemStorage
from user_app.models import Profile
import os


def render_all_posts(request):
    all_posts = Post.objects.all()
    return render(request,"post_app/all_posts.html",context={"all_posts":all_posts})   

def render_create_post(request):
    # Отримуємо усі теги з БД
    all_tags = Tag.objects.all()
    # Розміщуємо теги у контекст для передачі у HTML-шаблон
    context = {'tags': all_tags}
    # Якщо надсилається тип запиту POST, тобто користувач надсилає форму
    if request.method == "POST":
        # Отримуємо заголовок з HTML форми
        title = request.POST.get("title")
        # Отримуємо контент з HTML форми
        content = request.POST.get("content")

        # Отримуємо зображення з форми
        image = request.FILES.get("image")
        # Створоюємо (об'єднуємо) шлях для зображення
        image_path = os.path.join("images", "posts", image.name)
        # Створюємо об'єкт файлової системи для збереження зображення
        file_system = FileSystemStorage()
        # Зберігаємо зображення за вказаним шляхом
        file_system.save(image_path, image)

        # Отримуємо об'єкт користувача, що залогінився
        user = request.user
        # Отримуємо профіль користувача, що залогінився
        profile = Profile.objects.get(user=user)

        # Отримуємо теги, які обрав користувач у формі
        tags = request.POST.getlist("tags")
        
        
   
    return render(request, "post_app/create_post.html", context=context)