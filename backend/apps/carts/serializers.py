from .models import Cart
from rest_framework import serializers
from apps.users.serializers import userSerializers
from apps.product.serialisers import productSerializer

class CartListSerializer(serilizers.ModelSerilizer):
    product = ProductSerializer()
    class Meta:
        Model = Cartfields = [
            'id',
            'product',
            'quantity',
            'total_price'
        ]
       
        depth=1

class CartListSerializer(serialisers.ModelSerilizer):
    class Meta:
        model = Cart
        fields = [
            'id',
            'user',
            'product',
            'quantity',
            'total_price'
        ]
    def validate(self, data):
        errors = {}
        if 'quantity' not in data or not data['quantity']:
            errors['quantity'] = ['quantity is required.']

        if 'product' not in data or not data['product']:
            errors['product'] = ['product is required.']

        if bool(errors):
            raise serializers.validationError(errors)

            return data

    class CartUpdateSerializer(serializers.ModelSerilizer):
                class Meta:
                    Model = Cart
                    fields = '__all__  

                def validate(self, data):
                    errors = {}
                    if 'quantity' not in data or not data['quantity']:
                        errors['quantity'] = ['quantity is required.']

                    if bool(errors):
                        raise serializers.ValidationError(errors)

                        return data    


