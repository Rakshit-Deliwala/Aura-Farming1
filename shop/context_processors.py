from .cart import get_cart_items, get_cart_totals


def cart(request):
    items = get_cart_items(request)
    totals = get_cart_totals(request)
    return {
        'cart_items': items,
        'cart_total_amount': totals['total_amount'],
        'cart_total_quantity': totals['total_quantity'],
    }
