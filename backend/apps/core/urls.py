# backend/apps/core/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'products', views.ProductViewSet)
router.register(r'customers', views.CustomerViewSet)
router.register(r'suppliers', views.SupplierViewSet)
router.register(r'sales-orders', views.SalesOrderViewSet, basename='salesorder')
router.register(r'purchase-orders', views.PurchaseOrderViewSet, basename='purchaseorder')

# AGORA AS URLS SÃO RELATIVAS À 'api/'
urlpatterns = [
    # A view 'home' agora responderia em /api/
    path('', views.home, name='home'),
    
    # A rota do dashboard agora é simplesmente 'dashboard/'
    path('dashboard/', views.dashboard_stats, name='dashboard-stats'),
    
    # A linha abaixo inclui todas as rotas do router (products, customers, etc.)
    # O include vazio '' significa que elas estarão na raiz do que foi incluído.
    path('', include(router.urls)),
]