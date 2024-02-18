from rest_framework import serializers
from inventory.models import *


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'


class ProductRequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductRequest
        fields = "__all__"