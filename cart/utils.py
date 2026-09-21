from .models import Cart


def get_or_create_cart(request):
    """Retourne le panier courant : lié à l'utilisateur s'il est connecté,
    sinon lié à la session du navigateur (cliente invitée)."""
    if request.user.is_authenticated:
        cart, _ = Cart.objects.get_or_create(user=request.user, is_ordered=False)
        return cart

    if not request.session.session_key:
        request.session.create()
    session_key = request.session.session_key
    cart, _ = Cart.objects.get_or_create(session_key=session_key, user=None, is_ordered=False)
    return cart
