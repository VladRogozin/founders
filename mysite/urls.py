# mysite/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),  # Это отправляет корневой путь на accounts.urls
    path('shop/', include('shops.urls')),
    path('tasks/', include('tasks.urls')),
    path('my_site/', include('user_websites.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
