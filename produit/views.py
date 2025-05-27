from django.shortcuts import redirect, render, HttpResponse
from .models import Produit
from django.views import View

from .forms import ProduitForm
from django.contrib import messages
# Create your views here.


from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy


def index(request , *ards ,**kwargs):
    liste_produits = Produit.objects.all() #all()-> pour importer tout, #first()-> si c'est seulement pour le premier, filter(prix__gt=1000)gt-> > , lt-> <
    context = {
        'produits' : liste_produits,
        'nom': 'Produits de la boutique donald',
    }

    #return HttpResponse("<h1>Bienvenue dans django</h1>")
    return render(request , 'index.html', context)
    # return render(request , 'index.html', {}) #variable d'un dictionnaire vide ->{}

"""
class CreateProduct(View):
    def get(self , request , *args , **kwargs):
        return render(request, 'produits/create_product.html')
    
    #def post(self, request, *args, **kwargs):
        #pass
    def post(self, request, *args, **kwargs):
        try:
            nom = request.POST.get('nom')
            description = request.POST.get('description')
            prix = request.POST.get('prix')
            image = request.FILES.get('image')

            produit = Produit.objects.create(nom=nom , description=description, prix=prix, image=image)
            #produit.save() # ce n'est plus utile quand on utilise .objects.create

            if produit:
                return HttpResponse('Produit enregistré avec succès')
        except Exception as e:
            return HttpResponse('Erreur lors de l\'enregistrement du produit')
"""

#Generation du formulaire avec django
class CreateProduct(View):
    def get(self , request , *args , **kwargs):
        form = ProduitForm()
        return render(request, 'produits/create_product.html', {'form': form})
    
    def post(self, request , *args , **kwargs):
        form = ProduitForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Produit enregistré avec succès')
            return redirect('produits:index')
        else:
            messages.error(request, 'Erreur lors de l\'enregistrement du produit')
            return render(request, 'produits/create_product.html', {'form': form})

class UpdateProduct(View):
    def get(self, request, pk, *args, **kwargs):
        produit = Produit.objects.get(pk=pk)
        form = ProduitForm(instance=produit)
        return render(request, 'produits/produitUpdate.html', {'form': form})

    def post(self, request, pk, *args, **kwargs):
        produit = Produit.objects.get(pk=pk)
        form = ProduitForm(request.POST, request.FILES, instance=produit)
        if form.is_valid():
            form.save()
            messages.success(request, 'Produit modifié avec succès')
            return redirect('produits:index')
        else:
            messages.error(request, 'Erreur lors de la modification du produit')
            return render(request, 'produits/produitUpdate.html', {'form': form})

class DeleteProduct(View):
    def post(self, request, pk, *args, **kwargs):
        try:
            produit = Produit.objects.get(pk=pk)
            produit.delete()
            messages.success(request, 'Produit supprimé avec succès')
        except Produit.DoesNotExist:
            messages.error(request, 'Produit introuvable')
        return redirect('produits:index')




