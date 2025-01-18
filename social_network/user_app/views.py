from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.db.utils import IntegrityError
from django.contrib.auth import authenticate, login, logout
from .models import Profile

def render_registration(request):
    context = {}
    # Якщо метод запиту - POST (Якщо форма була відправлена)
    if request.method == 'POST':
        # Зберігаємо дані з форми у змінні
        username = request.POST.get('username')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')
        # Якщо користувач підтвердив пароль
        if password == password_confirm:
            try:
                # Створюємо користувача у БД
                User.objects.create_user(username= username, password= password)
                # Перенаправлення користувача на сторінку авторизації
                return redirect('login')
            # Відловлюємо помилку, якщо користувач намагається зареєструватись під вже існуючим ім'ям
            except IntegrityError:
                #  Вивести помилку у шаблоні про існуючого користувача 
                context = {'same_user' : True}
        else:
            # Вивести помилку у шаблоні про паролі, що не співпадають 
            context = {'same_password' : False}
    return render(request=request, template_name= "user_app/registration.html", context=context)


def render_login(request):
    context = {}
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        # Функція authenticate перевіря, чи існує користувач з таким логіном та паролем. Якщо існує - повртає об'єкт користувача. Якщо не існує - None
        user = authenticate(request = request,username = username, password = password)
        # Якщо такий користувач існує (Якщо користувач ввів правильний логін та пароль)
        if user:
            # Вхід користувача в акаунт
            login(request = request, user = user)
            return redirect('welcome')
        else:
            context = {"error" : True}
    return render(request=request, template_name='user_app/login.html', context=context)


def render_welcome(request):
    # Перевіряємо, чи залогінвся користувач
    if request.user.is_authenticated:
        return render(request=request, template_name= "user_app/welcome.html") 
    else:
        return redirect("login")
    

def logout_user(request):
    # Вихід користувача з акаунту
    logout(request)
    return redirect('login')

def render_all_profiles(request):
    all_profiles = Profile.objects.all()
    return render(request, 'user_app/all_profiles.html', {'all_profiles': all_profiles})
