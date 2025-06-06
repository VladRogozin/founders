from django.urls import path
from . import views

urlpatterns = [
    path('', views.shop_view, name='shop'),
    path('buy/<int:skin_id>/', views.buy_skin, name='buy_skin'),
    path('use/<int:skin_id>/', views.use_skin, name='use_skin'),
]