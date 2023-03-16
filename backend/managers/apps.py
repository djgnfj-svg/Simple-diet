from django.apps import AppConfig
from django.conf import settings


class ManagersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'managers'

    def ready(self) -> None:
        if settings.SCHEDULER_DEFAULT:
            from . import operator
            operator.start()
