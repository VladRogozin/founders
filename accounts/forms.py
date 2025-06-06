# accounts/forms.py
from django import forms
from django.contrib.auth.models import User
from .models import Profile

class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label='Пароль')

    class Meta:
        model = User
        fields = ['username', 'password']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
            # Создаём профиль с дефолтным аватаром
            Profile.objects.create(user=user, avatar='mistik.jpg')
        return user





class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar']