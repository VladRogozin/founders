from django.urls import path
from .views import CustomLoginView
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', views.logout_confirm, name='logout'),
]