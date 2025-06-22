from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)

    def __str__(self):
        return f'Profile for {self.user.username}'

    def get_avatar_url(self):
        if self.avatar:
            return self.avatar.url
        return '/static/images/hero-image.jpg'  # или путь к дефолтному аватару
