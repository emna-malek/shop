from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from accounts.decorators import allowed_users
from .forms import OrderCreateForm
from .models import CommandeItem, Commande
from cart.cart import Cart
from django.contrib.admin.views.decorators import staff_member_required
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import render_to_string

"""@allowed_users(allowed_roles=['customer'])"""


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            commande = form.save(commit=False)
            if cart.coupon:
                commande.coupon = cart.coupon
                commande.discount = cart.coupon.discount
            commande.save()
            for item in cart:
                CommandeItem.objects.create(
                    commande=commande,
                    produit=item['produit'],
                    prix=item['prix'],
                    quantity=item['quantity'])

            cart.clear()
            context = {
                'commande': commande,
            }
            request.session['commande_id'] = commande.id

            return redirect(reverse('payment:process'))
            # return render(request, 'order/created.html', context)

    else:
        form = OrderCreateForm()
    context = {
        'cart': cart,
        'form': form
    }
    return render(request, 'checkout.html', context)


"""
@staff_member_required
def admin_order_pdf(request, order_id):
    Order = get_object_or_404(order, id=order_id)
    html = render_to_string('order/pdf.html', {'order': Order})
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="order_{}.pdf"'.format(Order.id)
    weasyprint.HTML(string=html).write_pdf(response, stylesheets=[weasyprint.CSS(settings.STATIC_ROOT + 'css/pdf.css')])
    return response
"""
