# backend/config/urls.py

from django.contrib import admin
from django.urls import path, include
# 1. Importe a RedirectView
from django.views.generic.base import RedirectView

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