from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from boutique.models import Produit
from .cart import Cart
from cart.forms import CartAddProductForm
from coupons.forms import CouponApplyForm
from django.contrib import messages


# Create your views here.

@require_POST
def cart_add(request, produit_id):
    cart = Cart(request)
    produit = get_object_or_404(Produit, id=produit_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(
            produit=produit,
            quantity=cd['quantity'],
            update_quantity=cd['update']
        )
        messages.success(request, "Produit ajouté au panier avec succès")
    return redirect('cart:cart_detail')


def cart_remove(request, produit_id):
    cart = Cart(request)
    produit = get_object_or_404(Produit, id=produit_id)
    cart.remove(produit)
    messages.success(request, "Produit a bien été retiré de votre panier")
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'],  'update': True})
    coupon_apply_form = CouponApplyForm()
    context = {
        'cart': cart,
        'coupon_apply_form': coupon_apply_form
    }
    return render(request, 'cart/detail.html', context)
