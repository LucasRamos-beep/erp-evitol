# backend/apps/core/views.py

from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Sum, Count

# Importações de models
from .models import (
    Product, Customer, Supplier, 
    SalesOrder, PurchaseOrder
)
# Importações de serializers
from .serializers import (
    ProductSerializer, 
    CustomerSerializer, 
    SupplierSerializer, 
    SalesOrderSerializer,
    PurchaseOrderSerializer
)
# Importação dos filtros
from .filters import ProductFilter


def home(request):
    return HttpResponse("<h1>Parabéns! Seu servidor Django está no ar.</h1>")


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filterset_class = ProductFilter


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    filterset_fields = ['name', 'document']


class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    filterset_fields = ['name', 'document']


class SalesOrderViewSet(viewsets.ModelViewSet):
    # A linha 'queryset = ...' foi removida. O método get_queryset() agora cuida disso.
    serializer_class = SalesOrderSerializer
    filterset_fields = ['status', 'customer']

    def get_queryset(self):
        """
        Este método garante que o usuário só possa ver seus próprios pedidos de venda.
        """
        return SalesOrder.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        """
        Este método associa automaticamente o usuário logado ao novo pedido de venda criado.
        """
        serializer.save(user=self.request.user)


class PurchaseOrderViewSet(viewsets.ModelViewSet):
    # A linha 'queryset = ...' foi removida. O método get_queryset() agora cuida disso.
    serializer_class = PurchaseOrderSerializer
    filterset_fields = ['status', 'supplier']

    def get_queryset(self):
        """
        Este método garante que o usuário só possa ver seus próprios pedidos de compra.
        """
        return PurchaseOrder.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        """
        Este método associa automaticamente o usuário logado ao novo pedido de compra criado.
        """
        serializer.save(user=self.request.user)


@api_view(['GET'])
def dashboard_stats(request):
    """
    Retorna estatísticas agregadas para um dashboard.
    AGORA FILTRADO PELO USUÁRIO LOGADO.
    """
    user = request.user
    
    total_sales = SalesOrder.objects.filter(user=user, status='DONE').aggregate(total=Sum('total'))['total'] or 0.00
    open_orders_count = SalesOrder.objects.filter(user=user, status='OPEN').count()
    customer_count = Customer.objects.count() # (Este pode continuar geral)
    low_stock_products_count = Product.objects.filter(stock_quantity__lte=5).count()

    stats = {
        'total_sales_value': total_sales,
        'open_orders_count': open_orders_count,
        'customer_count': customer_count,
        'low_stock_products_count': low_stock_products_count,
    }
    
    return Response(stats)