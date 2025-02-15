from django import forms
from .models import Tag


class PostForm(forms.Form):
    title = forms.CharField(max_length=255, required=True)
    content = forms.CharField(widget=forms.Textarea(), required=True)
    image = forms.ImageField(required=True)
    tags = forms.ModelMultipleChoiceField(queryset = Tag.objects.all(), widget = forms.SelectMultiple, required = False)