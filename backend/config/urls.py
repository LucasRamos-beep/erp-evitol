# backend/config/urls.py

from django.contrib import admin
from django.urls import path, include
# 1. Importe a RedirectView
from django.views.generic.base import RedirectView

admin.site.site_header = "Painel de Controle - ERP Evitol"
admin.site.site_title = "Administração ERP Evitol"  
admin.site.index_title = "Bem-vindo ao Portal de Administração"

urlpatterns = [
    # 2. Adicione esta linha para redirecionar a raiz ('') para '/admin/'
    path('', RedirectView.as_view(url='/admin/', permanent=False), name='index'),
    
    path('admin/', admin.site.urls),
    
    # Nossas URLs da app 'core'
    path('api/', include('apps.core.urls')),
    
    # Rotas de autenticação
    path('api/auth/', include('dj_rest_auth.urls')),
    path('api/auth/registration/', include('dj_rest_auth.registration.urls')),
]