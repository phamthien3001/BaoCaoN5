from rest_framework import serializers
from .models import product_details


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = product_details # this is the model that is being serialized
        fields = ('product_name', 'price')