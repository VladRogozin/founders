from django.contrib.auth.models import User
from django.db import models


class Theory(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    image = models.ImageField(upload_to='theory_images/', blank=True, null=True)
    video = models.FileField(upload_to='theory_videos/', blank=True, null=True)
    audio = models.FileField(upload_to='theory_audio/', blank=True, null=True)

    def __str__(self):
        return self.title


class Task(models.Model):
    DIFFICULTY_CHOICES = [
        ('easy', 'Легкий'),
        ('medium', 'Средний'),
        ('hard', 'Сложный'),
    ]

    title = models.CharField(max_length=255)
    question = models.TextField()
    answer = models.TextField()
    image = models.ImageField(upload_to='task_images/', blank=True, null=True)
    video = models.FileField(upload_to='task_videos/', blank=True, null=True)
    audio = models.FileField(upload_to='task_audio/', blank=True, null=True)
    code = models.TextField(blank=True, null=True)
    difficulty = models.CharField(
        max_length=10,
        choices=DIFFICULTY_CHOICES,
        default='easy'
    )
    reward = models.PositiveIntegerField(default=0, help_text="Сколько очков получает пользователь за выполнение этого задания")
    theory = models.ForeignKey(Theory, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class TaskAnswer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    user_answer = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    # Добавьте это поле для админки, чтобы ставить "принято" или "нет"
    is_accepted = models.BooleanField(null=True, blank=True, default=None)

    def __str__(self):
        return f"Ответ от {self.user.username} на задание '{self.task.title}'"
