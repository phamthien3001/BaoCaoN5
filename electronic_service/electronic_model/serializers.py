from rest_framework import serializers
from .models import Electronic


class ElectronicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Electronic # this is the model that is being serialized
        fields = ('electronic_id', 'electronic_category', 'electronic_name', 'availability', 'price')