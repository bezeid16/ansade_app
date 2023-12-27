# ansade_app/admin.py

from django.contrib import admin
from .models import FamilleProduit, Produit, Panier, PanierProduit, Price, PointDeVente

# Register your models here

admin.site.register(FamilleProduit)
admin.site.register(Produit)
admin.site.register(Panier)
admin.site.register(PanierProduit)
admin.site.register(Price)
admin.site.register(PointDeVente)
