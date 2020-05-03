from django.db import models
from django.urls import reverse


# Create your models here.


class Catégorie(models.Model):
    nom = models.CharField(max_length=200, db_index=True)
    libellé = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('nom',)
        verbose_name = "Catégorie "
        verbose_name_plural = "Catégories "

    def __str__(self):
        return self.nom

    def get_absolute_url(self):
        return reverse('boutique:product_list_category', args=[self.libellé])


class Produit(models.Model):
    catégorie = models.ForeignKey(Catégorie, related_name='produit', on_delete=models.CASCADE)
    nom = models.CharField(max_length=200, db_index=True)
    libellé = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(blank=True)
    image1 = models.ImageField(blank=True)
    image2 = models.ImageField(blank=True)
    image3 = models.ImageField(blank=True)
    description = models.TextField(blank=True)
    prix = models.DecimalField(max_digits=20, decimal_places=2)
    stock = models.PositiveIntegerField()
    disponible = models.BooleanField(default=True)
    créé = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-créé',)
        index_together = (('id', 'libellé'),)
        verbose_name = "Produit"
        verbose_name_plural = "Produits"

    def __str__(self):
        return self.nom

    def get_absolute_url(self):
        return reverse('boutique:product_detail', args=[self.id, self.libellé])
