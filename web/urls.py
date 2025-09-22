# web/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('jidelni-listek/', views.jidelni_listek, name='jidelni_listek'),
    path('aktuality/', views.aktuality, name='aktuality'),
    path('kontakt/', views.kontakt, name='kontakt'), # Opravil jsem zde chybějící '='
]