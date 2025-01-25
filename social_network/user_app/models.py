from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    about_me = models.TextField()
    avatar = models.ImageField(upload_to = "images/avatars", null= True )

    def __str__(self):
        return self.user.username
    