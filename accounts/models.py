# accounts/models.py
from django.db import models
from django.contrib.auth.models import User
from shops.models import AvatarItem  # импортировать Skin из apps

from tasks.models import Task


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.CharField(max_length=100, default='mistik.jpg')  # убрали choices
    coins = models.PositiveIntegerField(default=0)
    points = models.PositiveIntegerField(default=0)
    owned_skins = models.ManyToManyField(AvatarItem, blank=True, related_name='owners')

    def __str__(self):
        return f'{self.user.username} Profile'


class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='notifications')
    message = models.TextField()
    is_accepted = models.BooleanField(default=False)  # задание принято или нет
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        status = "Принято" if self.is_accepted else "Отклонено"
        return f"Notification для {self.user.username} по заданию '{self.task.title}': {status}"