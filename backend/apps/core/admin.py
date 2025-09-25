# apps/core/admin.py

from django.contrib import admin
# Adicione os novos modelos na importação
from .models import Product, Customer, Supplier, SalesOrder, SalesOrderItem, PurchaseOrder, PurchaseOrderItem

# ... (SalesOrderItemInline e SalesOrderAdmin continuam aqui) ...
class SalesOrderItemInline(admin.TabularInline):
    model = SalesOrderItem
    extra = 1

@admin.register(SalesOrder)
class SalesOrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'status', 'total', 'created_at')
    list_filter = ('status', 'created_at')
    inlines = [SalesOrderItemInline]

# ADICIONE AS NOVAS CLASSES PARA PEDIDOS DE COMPRA
class PurchaseOrderItemInline(admin.TabularInline):
    model = PurchaseOrderItem
    extra = 1

@admin.register(PurchaseOrder)
class PurchaseOrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'supplier', 'status', 'total', 'created_at')
    list_filter = ('status', 'created_at')
    inlines = [PurchaseOrderItemInline]


# Registros simples para os outros modelos
admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Supplier)