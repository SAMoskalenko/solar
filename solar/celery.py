import os

from celery import Celery

from .settings import CELERY_PERIOD

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'solar.settings')

app = Celery('solar')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'add-at-melbourne-sunset': {
        'task': 'websites.tasks.checker',
        'schedule': CELERY_PERIOD,
    },
}
