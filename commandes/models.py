from django.db import models
from boutique.models import Produit
from decimal import Decimal
from django.core.validators import MinValueValidator, MaxValueValidator
from coupons.models import Coupons


class Commande (models.Model):
    nom = models.CharField(max_length=50)
    prénom = models.CharField(max_length=50)
    phone = models.CharField(max_length=200, null=True)
    email = models.EmailField()
    adresse = models.CharField(max_length=250)
    code_postal = models.CharField(max_length=50)
    ville = models.CharField(max_length=100)
    créé = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    payé = models.BooleanField(default=False)
    coupon = models.ForeignKey(Coupons, related_name='commandes', on_delete=models.CASCADE, null=True, blank=True)
    remise = models.IntegerField(default='0', validators=[MinValueValidator(0), MaxValueValidator(100)])

    class Meta:
        ordering = ('-créé',)
        verbose_name = "Commande"
        verbose_name_plural = "Commandes"

    def __str__(self):
        return 'Commande {}'.format(self.id)

    def get_total_cost(self):
        total_cost = sum(item.get_cost() for item in self.items.all())
        return total_cost - total_cost * (self.remise / Decimal(100))


class CommandeItem(models.Model):
    commande = models.ForeignKey(Commande, related_name='items', on_delete=models.CASCADE)
    produit = models.ForeignKey(Produit, related_name='commande_items', on_delete=models.CASCADE)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        verbose_name = "CommandeItem"
        verbose_name_plural = "CommandeItems"

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.prix * self.quantity
