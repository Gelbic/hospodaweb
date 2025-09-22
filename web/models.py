# web/models.py

from django.db import models
from django.utils import timezone

class KategorieMenu(models.Model):
    nazev = models.CharField(max_length=100, unique=True, verbose_name="Název kategorie")
    poradi = models.PositiveIntegerField(default=0, help_text="Pro seřazení kategorií na webu.")

    class Meta:
        verbose_name = "Kategorie menu"
        verbose_name_plural = "Kategorie menu"
        ordering = ['poradi']

    def __str__(self):
        return self.nazev

class PolozkaMenu(models.Model):
    nazev = models.CharField(max_length=200, verbose_name="Název položky")
    popis = models.TextField(blank=True, null=True, verbose_name="Popis")
    cena = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Cena v Kč")
    kategorie = models.ForeignKey(KategorieMenu, on_delete=models.CASCADE, related_name="polozky", verbose_name="Kategorie")
    alergeny = models.CharField(max_length=100, blank=True, null=True, verbose_name="Alergeny (čísla)")
    obrazek = models.ImageField(upload_to='menu_obrazky/', blank=True, null=True, verbose_name="Obrázek jídla")
    dostupne = models.BooleanField(default=True, verbose_name="Je dostupné?")

    class Meta:
        verbose_name = "Položka menu"
        verbose_name_plural = "Položky menu"
        ordering = ['kategorie__poradi', 'nazev']

    def __str__(self):
        return f"{self.nazev} ({self.cena} Kč)"

class Aktualita(models.Model):
    nadpis = models.CharField(max_length=255, verbose_name="Nadpis")
    obsah = models.TextField(verbose_name="Obsah článku")
    obrazek = models.ImageField(upload_to='aktuality/', blank=True, null=True, verbose_name="Hlavní obrázek")
    datum_vytvoreni = models.DateTimeField(default=timezone.now, verbose_name="Datum vytvoření")
    zverejneno = models.BooleanField(default=True, verbose_name="Zveřejněno?")

    class Meta:
        verbose_name = "Aktualita"
        verbose_name_plural = "Aktuality"
        ordering = ['-datum_vytvoreni']

    def __str__(self):
        return self.nadpis