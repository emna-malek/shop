from django.contrib import admin
from .models import CommandeItem, Commande
from import_export.admin import ImportExportActionModelAdmin
from django.urls import reverse
from django.utils.safestring import mark_safe

"""def order_pdf(obj):
    return mark_safe('<a href="{}">PDF</a>'.format(reverse('commandes:admin_order_pdf', args=[obj.id])))


order_pdf.short_description = 'Order PDF'
"""


class OrderItemAdmin(admin.TabularInline):
    model = CommandeItem
    raw_id_fields = ['produit']


class OrderAdmin(ImportExportActionModelAdmin):
    list_display = ('id', 'nom', 'prénom', 'adresse', 'email', 'ville', 'code_postal',)
    list_filter = ('payé', 'créé', 'updated',)
    search_fields = ['id', 'nom', 'prénom', 'email']
    inlines = [
        OrderItemAdmin,
    ]


admin.site.register(Commande, OrderAdmin)
