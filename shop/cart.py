from .models import Product


def _get_cart_session(request):
    cart = request.session.get('cart', {})
    if not isinstance(cart, dict):
        cart = {}
    return cart


def get_cart_items(request):
    cart = _get_cart_session(request)
    product_ids = []
    for pid in cart.keys():
        try:
            product_ids.append(int(pid))
        except (TypeError, ValueError):
            continue
    products = Product.objects.filter(id__in=product_ids)
    items = []
    for product in products:
        qty = cart.get(str(product.id), 0)
        if qty <= 0:
            continue
        line_total = product.price_inr * qty
        items.append({'product': product, 'quantity': qty, 'line_total': line_total})
    return items


def get_cart_totals(request):
    items = get_cart_items(request)
    total_amount = sum(i['line_total'] for i in items)
    total_quantity = sum(i['quantity'] for i in items)
    return {'total_amount': total_amount, 'total_quantity': total_quantity}


def add_to_cart(request, product_id, quantity=1):
    cart = _get_cart_session(request)
    key = str(product_id)
    cart[key] = cart.get(key, 0) + quantity
    request.session['cart'] = cart
    request.session.modified = True


def remove_from_cart(request, product_id):
    cart = _get_cart_session(request)
    key = str(product_id)
    if key in cart:
        del cart[key]
        request.session['cart'] = cart
        request.session.modified = True


def clear_cart(request):
    request.session['cart'] = {}
    request.session.modified = True
