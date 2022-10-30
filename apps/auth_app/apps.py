from django.apps import AppConfig


class AuthConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'auth'

class CoreConfig(AppConfig):
    name = 'compfactu.core'
