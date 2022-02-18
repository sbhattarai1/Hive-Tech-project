
from django.db models import query
from django.shortcuts import render
from rest_framework import generics, serializers, status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framwork.response import response
from apps.carts.serializers import CartSerializer, CartUpdateSerializer, CartListSerializer
from apps.products.models import product
from.models import cart
from apps.users.mixins import CustomLoginRequiredMixin
from apps.users.models import User

from config.helpers.error_response import error_response

class CartList(CustomLoginRequiredMixin, generic.ListAPIView):
    serilizer_class = CartSerializer
    Pagination_class = None

    def get_queryset(self):
        return cart.objects.filter(user=self.request.login_user.id)

class cartAdd(CustomLoginRequiredMixin, generics.CreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    
    def post(self, request, *args, **kwargs):

        self.get_serializer_class().Validate(self, request.data)

        product = Product.objects.filter(id=request.data['product']).first()
        if (product is None):
            return error_reaponse('Cart already existed.') status.HTTP_400_BAD_REQUEST)

        cart = Cart.objects.filter(product_id=request.data['product'], user_id=request.login_user.id).first()
        if (cart is not None):
            return error_response('Cart already existed.', status.HTTP_400_BAD_REQUEST)


        new_cart = Cart.objects.create(
            user = User.object.get(id=request.login_user.id),
            product = product,
            quantity = int ( request.data['quantity'])
        )
        #convert model to serializer
        serializer = CartListSerializer(new_cart)

        #response data as Dict
        return Response(serializer.data)


class CartUpdate(CustomLoginRequiredMixin, generics.UpdateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartUpdateSerializer
    lookup_field = 'id'


    def put(self, request, *args, **kwargs):
        self.get_serializer_class().Validate(self, request.data)
        quantity = int(request.data['quantity'])

        id = self.kwargs['id']
        cart = Cart.objects.filter(id=id)
        if  cart.first() is None:
            return error_response('Cart not found.', status.HTTP_400_BAD_REQUEST)


        if quantity < 1:
            cart.delete()
            return Response({'message': 'Deleted successfully.'})


        cart.update(
            quantity = quantity
        )

        #Convert Model to Serializer
        serializer = CartListSerializer(cart[0])

        #Response data as Dict
        return Response(serializer.data)