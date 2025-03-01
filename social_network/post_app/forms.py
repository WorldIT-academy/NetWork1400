from django import forms
from .models import Tag, Post
from django.core.exceptions import ValidationError


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = '__all__'

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not name[0].isalpha():
            raise ValidationError("Назва тегу повинна починатись з букви")
        return name


# Створюємо клас для форми, що пов'язана з моделлю
class PostForm(forms.ModelForm):
    # Клас, що відповідає за налаштування (конфігурацію) форми
    class Meta:
        # Підв'язуємо модель до форми
        model = Post
        # Відображаєм усі поля на сторінці, окрім поля автора
        fields = ["title", "content", "image", "tags"]
        # Здаємо зовнішній вигляд та атрибути для полів
        widgets = {
            "title": forms.TextInput(attrs= {"class": "form-field", "placeholder": "Заголовок"}),
            "content": forms.Textarea(attrs= {"class": "form-textarea"})
        }
    # Перезаписуємо метод save
    def save(self, author):
        # Створмо об'єкт поста, проте не зберігаємо у БД (за це відповідає commit=False)
        post = super().save(commit=False)
        # Додавання автора до поста та збереження змін
        post.author = author
        post.save()
        # Додавання теги до поста та збереження змін
        post.tags.set(self.cleaned_data.get('tags'))
        post.save()
        # Повертаємо пост
        return post

