# ansade_app/models.py

from django.db import models

class FamilleProduit(models.Model):
    id = models.AutoField(primary_key=True)
    label = models.TextField()

    def __str__(self):
        return self.label

class Produit(models.Model):
    id = models.AutoField(primary_key=True)
    label = models.TextField()
    price_unit = models.TextField()
    code = models.TextField()
    famille_produit = models.ForeignKey(FamilleProduit, on_delete=models.CASCADE)

    def __str__(self):
        return self.label

class Panier(models.Model):
    id = models.AutoField(primary_key=True)
    label = models.CharField(max_length=255)
    code = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.label

class PanierProduit(models.Model):
    id = models.AutoField(primary_key=True)
    price = models.ForeignKey('Price', on_delete=models.CASCADE)
    panier = models.ForeignKey(Panier, on_delete=models.CASCADE)
    ponderation = models.FloatField()

    def __str__(self):
        return f"{self.panier.label} - {self.price.value}"  # Modifié pour afficher le label du panier et la valeur du prix

class Price(models.Model):
    id = models.AutoField(primary_key=True)
    value = models.FloatField()
    date = models.DateField()
    point_de_vente = models.ForeignKey('PointDeVente', on_delete=models.CASCADE)
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.produit.label} - {self.value}"  # Modifié pour afficher le label du produit et la valeur du prix

class PointDeVente(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.TextField()
    wilaya = models.TextField()
    moughtaa = models.TextField()
    commune = models.TextField()
    gps_lat = models.FloatField()
    gps_long = models.FloatField()

    def __str__(self):
        return self.code