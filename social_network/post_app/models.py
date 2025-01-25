from django.db import models
from user_app.models import Profile


class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
    
class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to='images/posts')
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title