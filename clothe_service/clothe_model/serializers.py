from rest_framework import serializers
from .models import Clothe


class ClotheSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clothe # this is the model that is being serialized
        fields = ('clothe_id', 'clothe_category', 'clothe_name', 'availability', 'price')