from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_website, name='upload_website'),
    path('view/', views.view_website, name='view_website'),
]
