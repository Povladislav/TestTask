from django.apps import AppConfig


class LinkConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Link'

    def ready(self):
        import Link.signals
