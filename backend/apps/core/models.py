# backend/apps/core/models.py

from django.db import models
# 1. IMPORTE O MODELO USER
from django.contrib.auth.models import User

# ... (TimeStampedModel, Product, Customer, Supplier continuam iguais) ...
class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True

class Product(TimeStampedModel):
    name = models.CharField("Nome", max_length=200)
    description = models.TextField("Descrição", blank=True)
    price = models.DecimalField("Preço", max_digits=10, decimal_places=2, default=0)
    cost = models.DecimalField("Custo", max_digits=10, decimal_places=2, default=0)
    stock_quantity = models.DecimalField("Quantidade em Estoque", max_digits=10, decimal_places=2, default=0)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"

class Customer(TimeStampedModel):
    name = models.CharField("Nome", max_length=200)
    document = models.CharField("Documento (CPF/CNPJ)", max_length=20, unique=True)
    email = models.EmailField("E-mail", blank=True)
    phone = models.CharField("Telefone", max_length=20, blank=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

class Supplier(TimeStampedModel):
    name = models.CharField("Nome", max_length=200)
    document = models.CharField("Documento (CNPJ)", max_length=20, unique=True)
    email = models.EmailField("E-mail", blank=True)
    phone = models.CharField("Telefone", max_length=20, blank=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Fornecedor"
        verbose_name_plural = "Fornecedores"


class SalesOrder(TimeStampedModel):
    # ... (STATUS_CHOICES continua igual)
    STATUS_CHOICES = [
        ("DRAFT", "Rascunho"),
        ("OPEN", "Aberto"),
        ("DONE", "Concluído"),
        ("CANCELED", "Cancelado"),
    ]
    # 2. ADICIONE O CAMPO 'user'
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name="Usuário/Vendedor")
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT, verbose_name="Cliente")
    status = models.CharField("Status", max_length=10, choices=STATUS_CHOICES, default="DRAFT")
    total = models.DecimalField("Total", max_digits=10, decimal_places=2, default=0)
    
    # ... (o resto da classe, incluindo o método save, continua igual) ...
    def save(self, *args, **kwargs):
        old_status = None
        if self.pk:
            try:
                old_status = SalesOrder.objects.get(pk=self.pk).status
            except SalesOrder.DoesNotExist:
                pass
        super().save(*args, **kwargs)
        if self.status == 'DONE' and old_status != 'DONE':
            for item in self.items.all():
                product = item.product
                product.stock_quantity -= item.quantity
                product.save()
    def __str__(self):
        return f"Pedido {self.pk} - {self.customer.name}"
    class Meta:
        verbose_name = "Pedido de Venda"
        verbose_name_plural = "Pedidos de Venda"

# ... (SalesOrderItem continua igual) ...
class SalesOrderItem(models.Model):
    order = models.ForeignKey(SalesOrder, related_name="items", on_delete=models.CASCADE, verbose_name="Pedido")
    product = models.ForeignKey(Product, on_delete=models.PROTECT, verbose_name="Produto")
    quantity = models.DecimalField("Quantidade", max_digits=10, decimal_places=2)
    unit_price = models.DecimalField("Preço Unitário", max_digits=10, decimal_places=2)
    total = models.DecimalField("Total do Item", max_digits=10, decimal_places=2, editable=False)
    def save(self, *args, **kwargs):
        self.total = self.quantity * self.unit_price
        super().save(*args, **kwargs)
    def __str__(self):
        return f"{self.product.name} ({self.quantity})"
    class Meta:
        verbose_name = "Item do Pedido"
        verbose_name_plural = "Itens do Pedido"

class PurchaseOrder(TimeStampedModel):
    # ... (STATUS_CHOICES continua igual)
    STATUS_CHOICES = [
        ("DRAFT", "Rascunho"),
        ("SENT", "Enviado"),
        ("RECEIVED", "Recebido"),
        ("CANCELED", "Cancelado"),
    ]
    # 3. ADICIONE O CAMPO 'user'
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name="Usuário/Comprador")
    supplier = models.ForeignKey(Supplier, on_delete=models.PROTECT, verbose_name="Fornecedor")
    status = models.CharField("Status", max_length=10, choices=STATUS_CHOICES, default="DRAFT")
    total = models.DecimalField("Total", max_digits=10, decimal_places=2, default=0)
    
    # ... (o resto da classe, incluindo o método save, continua igual) ...
    def save(self, *args, **kwargs):
        old_status = None
        if self.pk:
            try:
                old_status = PurchaseOrder.objects.get(pk=self.pk).status
            except PurchaseOrder.DoesNotExist:
                pass
        super().save(*args, **kwargs)
        if self.status == 'RECEIVED' and old_status != 'RECEIVED':
            for item in self.items.all():
                product = item.product
                product.stock_quantity += item.quantity
                product.save()
    def __str__(self):
        return f"Pedido de Compra {self.pk} - {self.supplier.name}"
    class Meta:
        verbose_name = "Pedido de Compra"
        verbose_name_plural = "Pedidos de Compra"

# ... (PurchaseOrderItem continua igual) ...
class PurchaseOrderItem(models.Model):
    order = models.ForeignKey(PurchaseOrder, related_name="items", on_delete=models.CASCADE, verbose_name="Pedido")
    product = models.ForeignKey(Product, on_delete=models.PROTECT, verbose_name="Produto")
    quantity = models.DecimalField("Quantidade", max_digits=10, decimal_places=2)
    unit_cost = models.DecimalField("Custo Unitário", max_digits=10, decimal_places=2)
    total = models.DecimalField("Total do Item", max_digits=10, decimal_places=2, editable=False)
    def save(self, *args, **kwargs):
        self.total = self.quantity * self.unit_cost
        super().save(*args, **kwargs)
    def __str__(self):
        return f"{self.product.name} ({self.quantity})"
    class Meta:
        verbose_name = "Item de Compra"
        verbose_name_plural = "Itens de Compra"