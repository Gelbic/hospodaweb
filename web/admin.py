# web/admin.py

from django.contrib import admin
from .models import KategorieMenu, PolozkaMenu, Aktualita

@admin.register(KategorieMenu)
class KategorieMenuAdmin(admin.ModelAdmin):
    list_display = ('nazev', 'poradi')

@admin.register(PolozkaMenu)
class PolozkaMenuAdmin(admin.ModelAdmin):
    list_display = ('nazev', 'kategorie', 'cena', 'dostupne')
    list_filter = ('kategorie', 'dostupne')
    search_fields = ('nazev', 'popis')

@admin.register(Aktualita)
class AktualitaAdmin(admin.ModelAdmin):
    list_display = ('nadpis', 'datum_vytvoreni', 'zverejneno')
    list_filter = ('zverejneno',)
    search_fields = ('nadpis', 'obsah')

# Nastavení hlavičky administrace
admin.site.site_header = "Administrace webu U Svitavského Rytíře"
admin.site.site_title = "Admin portál"
admin.site.index_title = "Vítejte v administraci"