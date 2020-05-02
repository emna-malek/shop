from django import forms
from .models import Commande


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Commande
        fields = ('nom', 'prénom', 'phone', 'email', 'adresse', 'code_postal', 'ville',)
