from decimal import Decimal
from django.conf import settings
from boutique.models import Produit
from coupons.models import Coupons


class Cart(object):
    """docstring for Cart"""

    def __init__(self, request):
        """initalize the cart"""
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)

        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart
        self.coupon_id = self.session.get('coupon_id')

    def add(self, produit, quantity=1, update_quantity=False):

        produit_id = str(produit.id)
        if produit_id not in self.cart:
            self.cart[produit_id] = {'quantity': 0, 'prix': str(produit.prix)}

        if update_quantity:
            self.cart[produit_id]['quantity'] = quantity

        else:
            self.cart[produit_id]['quantity'] += quantity

        self.save()

    def save(self):

        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def remove(self, produit):
        produit_id = str(produit.id)
        if produit_id in self.cart:
            del self.cart[produit_id]
            self.save()

    def __iter__(self):

        produit_ids = self.cart.keys()

        produits = Produit.objects.filter(id__in=produit_ids)

        for produit in produits:
            self.cart[str(produit.id)]['produit'] = produit

        for item in self.cart.values():
            item['prix'] = Decimal(item['prix'])
            item['total_prix'] = item['prix'] * item['quantity']
            yield item

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        return sum(Decimal(item['prix']) * item['quantity'] for item in self.cart.values())

    def get_total_quantity(self):
        return sum(item['quantity'] for item in self.cart.values())

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True

    @property
    def coupon(self):
        if self.coupon_id:
            return Coupons.objects.get(id=self.coupon_id)
        return None

    def get_discount(self):
        if self.coupon:
            return (self.coupon.discount / Decimal('100')) * self.get_total_price()
        return Decimal('0')

    def get_total_price_after_discount(self):
        return self.get_total_price() - self.get_discount()
