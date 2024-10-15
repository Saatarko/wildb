from rest_framework import serializers

from .models import Product


# Пустой сериализатор для корректного отображения схемы

class TaskIdSerializer(serializers.Serializer):
    task_id = serializers.CharField()

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['article', 'name', 'brand', 'price', 'discount', 'stock_quantity', 'warehouses']