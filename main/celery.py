from __future__ import absolute_import, unicode_literals

import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'main.settings')

app = Celery('main')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.update(
    CELERY_RESULT_BACKEND = None,  # Configuración del backend
)

app.autodiscover_tasks(['vuelos'])  # Busca tareas en la app vuelos