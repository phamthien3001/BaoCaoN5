from rest_framework import serializers
from .models import Shoes


class ShoesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shoes # this is the model that is being serialized
        fields = ('shoes_id', 'shoes_category', 'shoes_name', 'availability', 'price')