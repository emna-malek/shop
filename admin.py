
from boutique.models import Catégorie
from boutique.models import Produit
from django.contrib import admin


# Register your models here.


class CatégorieAdmin(admin.ModelAdmin):
    # Admin view for category

    list_display = ('nom', 'libellé',)
    search_fields = ['nom', ]
    prepopulated_fields = {'libellé': ('nom',)}


admin.site.register(Catégorie, CatégorieAdmin)


class ProduitAdmin(admin.ModelAdmin):
    # Admin view for product

    list_display = ('nom', 'libellé', 'catégorie', 'prix', 'stock', 'disponible', 'créé', 'updated',)
    list_filter = ('disponible', 'créé', 'updated', 'catégorie',)
    list_editable = ('prix', 'stock', 'disponible',)
    search_fields = ['nom', ]
    prepopulated_fields = {'libellé': ('nom',)}


admin.site.register(Produit, ProduitAdmin)
