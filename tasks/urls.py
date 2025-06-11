# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('pentagon/', views.pentagon, name='pentagon_page'),
    path('tasks/', views.task_list, name='task_list'),
]
