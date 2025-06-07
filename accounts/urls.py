# accounts/urls.py

from django.urls import path
from . import views
from .views import CustomLoginView

urlpatterns = [
    path('', views.lending_page, name='lending'),  # Это отвечает за главную страницу
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', views.logout_confirm, name='logout'),
]
