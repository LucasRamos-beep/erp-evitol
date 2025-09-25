# backend/config/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Esta linha conecta à configuração de URL do seu aplicativo
    path('api/', include('apps.core.urls')), 
    
    # Rotas de autenticação
    path('api/auth/', include('dj_rest_auth.urls')),
    path('api/auth/registration/', include('dj_rest_auth.registration.urls')),
]