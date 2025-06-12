from django.urls import path
from . import views

urlpatterns = [
    path('', views.shop_view, name='shop'),
    path('buy/<str:model_name>/<int:item_id>/', views.buy_item, name='buy_item'),
    path('use/<str:model_name>/<int:item_id>/', views.use_item, name='use_item'),
]