from django.db import models
from django.contrib.auth.models import User

class UserWebsite(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    html_file = models.FileField(upload_to='user_sites/html/')
    css_file = models.FileField(upload_to='user_sites/css/')
    js_file = models.FileField(upload_to='user_sites/js/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Сайт пользователя {self.user.username}"