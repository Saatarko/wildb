from __future__ import absolute_import
import os
from celery import Celery
import eventlet
eventlet.monkey_patch()



os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wildberries_project.settings')

app = Celery('wildberries_project')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

# Эта строка нужна, чтобы убедиться, что объект `app` доступен в пространстве имен модуля
__all__ = ('app',)
