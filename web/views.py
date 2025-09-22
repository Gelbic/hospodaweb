# web/views.py

from django.shortcuts import render
from .models import Aktualita, KategorieMenu, PolozkaMenu

def index(request):
    # Pro úvodní stránku vybereme 3 nejnovější aktuality
    posledni_aktuality = Aktualita.objects.filter(zverejneno=True)[:3]
    context = {
        'aktuality': posledni_aktuality
    }
    return render(request, 'web/index.html', context)

def jidelni_listek(request):
    # Načteme všechny kategorie, které mají alespoň jednu dostupnou položku
    kategorie = KategorieMenu.objects.filter(polozky__dostupne=True).distinct()
    context = {
        'kategorie': kategorie
    }
    return render(request, 'web/jidelni_listek.html', context)

def aktuality(request):
    # Zobrazíme všechny zveřejněné aktuality
    vsechny_aktuality = Aktualita.objects.filter(zverejneno=True)
    context = {
        'aktuality': vsechny_aktuality
    }
    return render(request, 'web/aktuality.html', context)

def kontakt(request):
    # Kontaktní stránka nepotřebuje žádná data z databáze
    return render(request, 'web/kontakt.html')