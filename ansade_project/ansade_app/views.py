# ansade_app/views.py
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView ,View
from .models import FamilleProduit, Produit, Panier, PanierProduit, Price, PointDeVente
from django.shortcuts import render, get_object_or_404
from .resources import FamilleProduitResource, ProduitResource ,PanierResource ,PanierProduitResource ,PriceResource ,PointDeVenteResource # Importez d'autres ressources nécessaires
from django.http import HttpResponse
from tablib import Dataset
from django.contrib import messages
from django.shortcuts import redirect
import csv
from django.views.generic import TemplateView
from django.http import JsonResponse
from django.db.models import Sum, Avg
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


class PricePredictionView(View):
    template_name = 'ansade_app/price_prediction.html'

    def get(self, request, product_id):
        prices = Price.objects.filter(produit__id=product_id).order_by('date')

        if len(prices) < 2:
            return JsonResponse({'error': 'Insufficient data for prediction'})

        # Préparation des données pour la régression linéaire
        dates = [(price.date - prices[0].date).days for price in prices]
        values = [price.value for price in prices]

        # Création d'un modèle de régression linéaire
        model = LinearRegression()

        # Reshape pour s'assurer que les données sont 2D
        dates = [[date] for date in dates]

        # Division des données en ensembles d'entraînement et de test
        X_train, X_test, y_train, y_test = train_test_split(dates, values, test_size=0.2, random_state=42)

        # Entraînement du modèle
        model.fit(X_train, y_train)


        predictions = model.predict(X_test)

        # Calcul de la performance du modèle (à titre informatif)
        accuracy = model.score(X_test, y_test)

        # Prédictions pour les prochaines dates (30 jours de plus que la dernière date connue)
        future_dates = [[date] for date in range(dates[-1][0] + 1, dates[-1][0] + 31)]
        future_predictions = model.predict(future_dates)

        predictions_list = [{'date': date, 'actual_price': actual_price, 'predicted_price': predicted_price} 
                    for date, actual_price, predicted_price in zip(X_test, y_test, predictions)]

        future_predictions_list = [{'date': date, 'predicted_price': predicted_price} 
                        for date, predicted_price in zip(future_dates, future_predictions)]



        
        context = {
                    'predictions': predictions_list,
                    'future_predictions': future_predictions_list,
                    'accuracy': accuracy,
                }


        return render(request, self.template_name, context)

def calculate_inpc(request):
    paniers = Panier.objects.all()

    # Supposons que le panier sélectionné est le premier panier de la liste
    panier_selected = paniers.first()

    total_cost_current = 0.0
    total_cost_base = 0.0

    # Récupérez la première date présente dans le modèle Price
    base_date = Price.objects.earliest('date').date

    # Calcul de la somme du coût actuel pour tous les paniers
    for panier in paniers:
        produits_panier = PanierProduit.objects.filter(panier=panier)
        for panier_produit in produits_panier:
            prix_actuel = Price.objects.filter(produit=panier_produit.price.produit, date__lte=panier_produit.price.date).latest('date')
            cost_product_current = prix_actuel.value * panier_produit.ponderation
            total_cost_current += cost_product_current

    # Calcul de la somme du coût total des paniers à la date de référence (base)
    produits_base = PanierProduit.objects.filter(panier=panier_selected, price__date=base_date)
    for produit_base in produits_base:
        total_cost_base += produit_base.price.value * produit_base.ponderation

    # Vérifiez si total_cost_base est différent de zéro avant de calculer l'IPC
    if total_cost_base != 0:
        # Calculez la somme des IPC agrégés
        ipc_agrege_sum = (total_cost_current / total_cost_base) * 100
    else:
        # Gérez le cas où total_cost_base est égal à zéro (par exemple, attribuez une valeur par défaut à la somme des IPC agrégés)
        ipc_agrege_sum = 0.0  # Choisissez une valeur appropriée

    context = {
        'paniers': paniers,
        'ipc_agrege_sum': ipc_agrege_sum,
    }

    return render(request, 'calculate_inpc.html', context)

class ProductPriceChartView(View):
    template_name = 'ansade_app/product_price_chart.html'

    def get(self, request, product_id):
        product = Produit.objects.get(id=product_id)
        prices = (
            Price.objects.filter(produit__id=product_id)
            .values('date')
            .annotate(average_price=Avg('value'))
            .order_by('date')
        )

        labels = [price['date'].strftime("%Y-%m-%d") for price in prices]
        values = [price['average_price'] for price in prices]


        context = {
            'product': product,
            'labels': labels,
            'values': values,
        }

        return render(request, self.template_name, context)

def select_product(request):
    products = Produit.objects.all()
    return render(request, 'ansade_app/select_product.html', {'products': products})

def select_product1(request):
    products = Produit.objects.all()
    return render(request, 'ansade_app/select_product1.html', {'products': products})
#famille produit
def export_famille_produit(request):
    famille_produit_resource = FamilleProduitResource()
    dataset = famille_produit_resource.export()
    response = HttpResponse(dataset.csv, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="famille_produit.csv"'
    return response

def import_famille_produit(request):
    result_message = None

    if request.method == 'POST':
        famille_produit_resource = FamilleProduitResource()
        dataset = Dataset()
        new_famille_produit_file = request.FILES['myfile']

        if not new_famille_produit_file.name.endswith('.csv'):
            messages.error(request, 'Le fichier doit être un CSV.')
        else:
            try:
                imported_data = dataset.load(new_famille_produit_file.read().decode('utf-8'), format='csv')
                famille_produit_resource.import_data(dataset, dry_run=False)
                messages.success(request, 'Import réussi.')
            except Exception as e:
                messages.error(request, f'Une erreur s\'est produite lors de l\'import : {e}')

            result_message = list(messages.get_messages(request))  # Convert messages to a list

    return render(request, 'import_result.html', {'result_message': result_message})

#produit
def export_produit(request):
    produit_resource = ProduitResource()
    dataset = produit_resource.export()
    response = HttpResponse(dataset.csv, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="produit.csv"'
    return response

def import_produit(request):
    result_message = None

    if request.method == 'POST':
        produit_resource = ProduitResource()
        dataset = Dataset()
        new_produit_file = request.FILES['myfile']

        if not new_produit_file.name.endswith('.csv'):
            messages.error(request, 'Le fichier doit être un CSV.')
        else:
            try:
                imported_data = dataset.load(new_produit_file.read().decode('utf-8'))
                produit_resource.import_data(dataset, dry_run=False)
                messages.success(request, 'Import réussi.')
            except Exception as e:
                messages.error(request, f'Une erreur s\'est produite lors de l\'import : {e}')

            result_message = list(messages.get_messages(request))  # Convert messages to a list

    return render(request, 'import_result.html', {'result_message': result_message})

#Panier
def export_Panier(request):
    Panier_resource = PanierResource()
    dataset = Panier_resource.export()
    response = HttpResponse(dataset.csv, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="Panier.csv"'
    return response

def import_Panier(request):
    result_message = None

    if request.method == 'POST':
        Panier_resource = PanierResource()
        dataset = Dataset()
        new_Panier_file = request.FILES['myfile']

        if not new_Panier_file.name.endswith('.csv'):
            messages.error(request, 'Le fichier doit être un CSV.')
        else:
            try:
                imported_data = dataset.load(new_Panier_file.read().decode('utf-8'))
                Panier_resource.import_data(dataset, dry_run=False)
                messages.success(request, 'Import réussi.')
            except Exception as e:
                messages.error(request, f'Une erreur s\'est produite lors de l\'import : {e}')

            result_message = list(messages.get_messages(request))  # Convert messages to a list

    return render(request, 'import_result.html', {'result_message': result_message})

#PanierProduit
def export_PanierProduit(request):
    PanierProduit_resource = PanierProduitResource()
    dataset = PanierProduit_resource.export()
    response = HttpResponse(dataset.csv, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="PanierProduit.csv"'
    return response

def import_PanierProduit(request):
    result_message = None

    if request.method == 'POST':
        PanierProduit_resource = PanierProduitResource()
        dataset = Dataset()
        new_PanierProduit_file = request.FILES['myfile']

        if not new_PanierProduit_file.name.endswith('.csv'):
            messages.error(request, 'Le fichier doit être un CSV.')
        else:
            try:
                imported_data = dataset.load(new_PanierProduit_file.read().decode('utf-8'))
                PanierProduit_resource.import_data(dataset, dry_run=False)
                messages.success(request, 'Import réussi.')
            except Exception as e:
                messages.error(request, f'Une erreur s\'est produite lors de l\'import : {e}')

            result_message = list(messages.get_messages(request))  # Convert messages to a list

    return render(request, 'import_result.html', {'result_message': result_message})

#Price
def export_Price(request):
    Price_resource = PriceResource()
    dataset = Price_resource.export()
    response = HttpResponse(dataset.csv, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="Price.csv"'
    return response

def import_Price(request):
    result_message = None

    if request.method == 'POST':
        price_resource = PriceResource()
        dataset = Dataset()
        new_price_file = request.FILES['myfile']

        if not new_price_file.name.endswith('.csv'):
            messages.error(request, 'Le fichier doit être un CSV.')
        else:
            try:
                imported_data = dataset.load(new_price_file.read().decode('utf-8'))
                price_resource.import_data(dataset, dry_run=False)
                messages.success(request, 'Import réussi.')
            except Exception as e:
                messages.error(request, f'Une erreur s\'est produite lors de l\'import : {e}')

            result_message = list(messages.get_messages(request))  # Convert messages to a list

    return render(request, 'import_result.html', {'result_message': result_message})

#PointDeVente
def export_PointDeVente(request):
    PointDeVente_resource = PointDeVenteResource()
    dataset = PointDeVente_resource.export()
    response = HttpResponse(dataset.csv, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="PointDeVente.csv"'
    return response

def import_PointDeVente(request):
    result_message = None

    if request.method == 'POST':
        PointDeVente_resource = PointDeVenteResource()
        dataset = Dataset()
        new_PointDeVente_file = request.FILES['myfile']

        if not new_PointDeVente_file.name.endswith('.csv'):
            messages.error(request, 'Le fichier doit être un CSV.')
        else:
            try:
                imported_data = dataset.load(new_PointDeVente_file.read().decode('utf-8'))
                PointDeVente_resource.import_data(dataset, dry_run=False)
                messages.success(request, 'Import réussi.')
            except Exception as e:
                messages.error(request, f'Une erreur s\'est produite lors de l\'import : {e}')

            result_message = list(messages.get_messages(request))  # Convert messages to a list

    return render(request, 'import_result.html', {'result_message': result_message})


def home(request):

    return render(request, 'ansade_app/home.html')

# FamilleProduit Views
class FamilleProduitListView(ListView):
    model = FamilleProduit

class FamilleProduitDetailView(DetailView):
    model = FamilleProduit

class FamilleProduitCreateView(CreateView):
    model = FamilleProduit
    fields = '__all__'
    success_url = reverse_lazy('famille_produit_list')  # Redirect to the list view after creating

class FamilleProduitUpdateView(UpdateView):
    model = FamilleProduit
    fields = '__all__'
    success_url = reverse_lazy('famille_produit_list')  # Redirect to the list view after updating

class FamilleProduitDeleteView(DeleteView):
    model = FamilleProduit
    success_url = reverse_lazy('famille_produit_list')  # Redirect to the list view after deleting

# Produit Views
class ProduitListView(ListView):
    model = Produit

class ProduitDetailView(DetailView):
    model = Produit

class ProduitCreateView(CreateView):
    model = Produit
    fields = '__all__'
    success_url = reverse_lazy('produit_list')  # Redirect to the list view after creating

class ProduitUpdateView(UpdateView):
    model = Produit
    fields = '__all__'
    success_url = reverse_lazy('produit_list')  # Redirect to the list view after updating

class ProduitDeleteView(DeleteView):
    model = Produit
    success_url = reverse_lazy('produit_list')  # Redirect to the list view after deleting

# Panier Views
class PanierListView(ListView):
    model = Panier

class PanierDetailView(DetailView):
    model = Panier

class PanierCreateView(CreateView):
    model = Panier
    fields = '__all__'
    success_url = reverse_lazy('panier_list')  # Redirect to the list view after creating

class PanierUpdateView(UpdateView):
    model = Panier
    fields = '__all__'
    success_url = reverse_lazy('panier_list')  # Redirect to the list view after updating

class PanierDeleteView(DeleteView):
    model = Panier
    success_url = reverse_lazy('panier_list')  # Redirect to the list view after deleting



class PanierProduitListView(ListView):
    model = PanierProduit
    template_name = 'ansade_app/panierproduit_list.html'  # Specify the template name

class PanierProduitDetailView(DetailView):
    model = PanierProduit
    template_name = 'ansade_app/panierproduit_detail.html'  # Specify the template name

class PanierProduitCreateView(CreateView):
    model = PanierProduit
    template_name = 'ansade_app/panierproduit_form.html'  # Specify the template name
    fields = '__all__'
    success_url = reverse_lazy('panier_produit_list')  # Redirect to the list view after creating

class PanierProduitUpdateView(UpdateView):
    model = PanierProduit
    template_name = 'ansade_app/panierproduit_form.html'  # Specify the template name
    fields = '__all__'
    success_url = reverse_lazy('panier_produit_list')  # Redirect to the list view after updating

class PanierProduitDeleteView(DeleteView):
    model = PanierProduit
    template_name = 'ansade_app/panierproduit_confirm_delete.html'  # Specify the template name
    success_url = reverse_lazy('panier_produit_list')  # Redirect to the list view after deleting


# Price Views
class PriceListView(ListView):
    model = Price

class PriceDetailView(DetailView):
    model = Price

class PriceCreateView(CreateView):
    model = Price
    fields = '__all__'
    success_url = reverse_lazy('price_list')  # Redirect to the list view after creating

class PriceUpdateView(UpdateView):
    model = Price
    fields = '__all__'
    success_url = reverse_lazy('price_list')  # Redirect to the list view after updating

class PriceDeleteView(DeleteView):
    model = Price
    success_url = reverse_lazy('price_list')  # Redirect to the list view after deleting

# PointDeVente Views
class PointDeVenteListView(ListView):
    model = PointDeVente

class PointDeVenteDetailView(DetailView):
    model = PointDeVente

class PointDeVenteCreateView(CreateView):
    model = PointDeVente
    fields = ['code', 'wilaya', 'moughtaa', 'commune', 'gps_lat', 'gps_long']
    success_url = reverse_lazy('point_de_vente_list')  # Redirect to the list view after creating

class PointDeVenteUpdateView(UpdateView):
    model = PointDeVente
    fields = ['code', 'wilaya', 'moughtaa', 'commune', 'gps_lat', 'gps_long']
    success_url = reverse_lazy('point_de_vente_list')  # Redirect to the list view after updating

class PointDeVenteDeleteView(DeleteView):
    model = PointDeVente
    fields = ['code', 'wilaya', 'moughtaa', 'commune', 'gps_lat', 'gps_long']
    success_url = reverse_lazy('point_de_vente_list')  # Redirect to the list view after deleting

