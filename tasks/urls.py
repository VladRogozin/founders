# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('pentagon/', views.pentagon, name='pentagon_page'),
    path('rocket_start/', views.rocket_start, name='rocket_start'),
    path('tasks/', views.task_list, name='task_list'),
]
