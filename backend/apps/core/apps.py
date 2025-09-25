# apps/core/apps.py

from django.apps import AppConfig

class CoreConfig(AppConfig):  # <-- O nome que precisamos é 'CoreConfig'
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.core'