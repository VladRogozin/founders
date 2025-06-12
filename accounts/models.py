# accounts/models.py
from django.db import models
from django.contrib.auth.models import User
from shops.models import AvatarItem, ComputerItem

from tasks.models import Task




class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.CharField(max_length=100, default='mistik.jpg')  # можно убрать позже
    coins = models.PositiveIntegerField(default=0)
    points = models.PositiveIntegerField(default=0)
    owned_skins = models.ManyToManyField(AvatarItem, blank=True, related_name='owners')
    owned_computeritems = models.ManyToManyField(ComputerItem, blank=True, related_name='owned_computeritems')

    active_skin = models.ForeignKey(
        AvatarItem,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='active_users'
    )
    active_computer = models.ForeignKey(
        ComputerItem,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='active_users'
    )

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