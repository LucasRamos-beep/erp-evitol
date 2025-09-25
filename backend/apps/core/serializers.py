# apps/core/serializers.py

from rest_framework import serializers
# CORREÇÃO: Adicionados PurchaseOrder e PurchaseOrderItem às importações principais
from .models import (
    Product, Customer, Supplier, 
    SalesOrder, SalesOrderItem,
    PurchaseOrder, PurchaseOrderItem
)


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'


# --- Serializers de Venda ---

class SalesOrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesOrderItem
        fields = ['id', 'product', 'quantity', 'unit_price', 'total']


class SalesOrderSerializer(serializers.ModelSerializer):
    items = SalesOrderItemSerializer(many=True)
    customer_name = serializers.CharField(source='customer.name', read_only=True)

    class Meta:
        model = SalesOrder
        fields = ['id', 'customer', 'customer_name', 'status', 'total', 'items', 'created_at']

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        order = SalesOrder.objects.create(**validated_data)
        
        total_pedido = 0
        for item_data in items_data:
            item = SalesOrderItem.objects.create(order=order, **item_data)
            total_pedido += item.total
            
        order.total = total_pedido
        order.save()
        
        return order

# --- Serializers de Compra ---

class PurchaseOrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrderItem
        fields = ['id', 'product', 'quantity', 'unit_cost', 'total']


class PurchaseOrderSerializer(serializers.ModelSerializer):
    items = PurchaseOrderItemSerializer(many=True)
    supplier_name = serializers.CharField(source='supplier.name', read_only=True)

    class Meta:
        model = PurchaseOrder
        fields = ['id', 'supplier', 'supplier_name', 'status', 'total', 'items', 'created_at']

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        order = PurchaseOrder.objects.create(**validated_data)
        
        total_pedido = 0
        for item_data in items_data:
            item = PurchaseOrderItem.objects.create(order=order, **item_data)
            total_pedido += item.total
            
        order.total = total_pedido
        order.save()
        
        return order