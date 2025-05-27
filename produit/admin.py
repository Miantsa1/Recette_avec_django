from django.contrib import admin

# enregistrer les tables
from .models import Produit

#admin.site.register(Produit) #ce n'est pas encore sous forme de tableau

#Pour qu'il s'affiche en tableau

@admin.register(Produit) #mettre un decorateur
class ProduitAdmin(admin.ModelAdmin):
    list_display = ('nom' , 'prix' , 'description' , 'image' )

# Register your models here.
