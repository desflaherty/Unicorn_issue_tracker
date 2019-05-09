from django.shortcuts import get_object_or_404
from features.models import Features


def cart_contents(request):
    """
    Ensures that the cart contents are available when rendering
    every page
    """
    cart = request.session.get('cart', {})

    cart_items = []
    upvote_list = []
    price = 100
    total = 0
    feature_count = 0
    for id, quantity in cart.items():
        feature = get_object_or_404(Features, pk=id)
        upvote_list.append(id)
        feature_count += quantity
        total += quantity * price
        cart_items.append({'id': id, 'quantity': quantity,
                           'feature': feature, 'price': price})

    return {'feature_count': feature_count,
            'cart_items': cart_items,
            'total': total,
            'upvote_list': upvote_list}