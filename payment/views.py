from django.shortcuts import render, get_object_or_404
from decimal import Decimal
from django.conf import settings
from django.urls import reverse
from paypal.standard.forms import PayPalPaymentsForm
from commandes.models import Commande
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def payment_done(request):
    return render(request, 'payment/done.html')


@csrf_exempt
def payment_canceled(request):
    return render(request, 'payment/canceled.html')


def payment_process(request):
    commande_id = request.session.get('commande_id')
    commandes = get_object_or_404(Commande, id=commande_id)
    host = request.get_host()

    paypal_dict = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount': '%.2f' % commandes.get_total_cost().quantize(Decimal('.01')),
        'item_name': 'Commande{}'.format(Commande.id),
        'invoice': str(commandes.id),
        'currency_code': 'USD',
        'notify_url': 'http://{}{}'.format(host, reverse('paypal-ipn')),
        'return_url': 'http://{}{}'.format(host, reverse('payment:done')),
        'cancel_return': 'http://{}{}'.format(host, reverse('payment:canceled')),
    }
    form = PayPalPaymentsForm(initial=paypal_dict)
    context = {
        'commande': commandes,
        'form': form,
    }
    return render(request, 'payment/process.html', context)
