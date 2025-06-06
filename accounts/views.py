from django.shortcuts import render, redirect
from .forms import UserRegisterForm, ProfileForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
import os
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import ProfileForm
from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы успешно зарегистрировались! Можете войти.')
            return redirect('login')  # или куда хочешь перенаправить после регистрации
    else:
        form = UserRegisterForm()
    return render(request, 'accounts/register.html', {'form': form})



from .models import Notification  # обязательно

@login_required
def profile(request):
    profile = request.user.profile

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=profile)

    avatar_static_path = os.path.join(
        settings.BASE_DIR, 'static', 'base_img_profile', profile.avatar
    )
    if os.path.exists(avatar_static_path):
        avatar_url = settings.STATIC_URL + 'base_img_profile/' + profile.avatar
    else:
        avatar_url = settings.MEDIA_URL + profile.avatar

    # ⚠️ Добавляем получение уведомлений, отсортированных по дате
    notifications = Notification.objects.filter(user=request.user).order_by('-created_at')

    context = {
        'form': form,
        'avatar_url': avatar_url,
        'username': request.user.username,
        'coins': profile.coins,
        'points': profile.points,
        'notifications': notifications,  # ✅ Добавляем в контекст
    }

    return render(request, 'accounts/profile.html', context)


from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy

class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'

# accounts/views.py
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required
def logout_confirm(request):
    if request.method == 'POST':
        # Пользователь подтвердил выход — разлогиниваем и редиректим
        logout(request)
        return redirect('login')
    # Иначе показываем страницу подтверждения
    return render(request, 'accounts/logout_confirm.html')