# hospoda_projekt/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('web.urls')), # <-- Všechny ostatní URL hledej v aplikaci 'web'
]

# Toto přidáme jen v DEBUG režimu pro obsluhu nahraných souborů
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)