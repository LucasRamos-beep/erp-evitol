# backend/config/settings.py
import os
import dj_database_url # Importe no topo

# ...

# Mude o DEBUG para ler de uma variável de ambiente
# O 'False' é o padrão se a variável não for encontrada
DEBUG = os.environ.get('DEBUG', 'False').lower() == 'true'

# Pegue o endereço do seu futuro site do Render.
# Adicione '*' para permitir todos os hosts durante a configuração inicial.
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '127.0.0.1,localhost').split(',')


# ... (INSTALLED_APPS continua igual)

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', # Adicione o Whitenoise aqui
    'django.contrib.sessions.middleware.SessionMiddleware',
    # ... resto do middleware
]

# ...

# Configuração do Banco de Dados para ler a URL do Render
DATABASES = {
    'default': dj_database_url.config(
        default=f'sqlite:///{BASE_DIR / "db.sqlite3"}',
        conn_max_age=600
    )
}

# ...

# Configuração de Arquivos Estáticos com Whitenoise
STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles' # Django coletará os arquivos estáticos aqui
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'