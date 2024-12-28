from rest_framework import viewsets
from cart.models import Cart
from .serializer import CartSerializer

class CartViewSet(viewsets.ModelViewSet):
    queryset =Cart.objects.all()
    serializer_class= CartSerializer