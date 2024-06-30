from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from decouple import config

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "letapay_backend.settings")

app = Celery(
    "letapay_backend", broker=config("REDIS_URL"), backend=config("REDIS_URL")
)

app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()
