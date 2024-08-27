import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DjTodos.settings")

app = Celery("DjTodos")

app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()


 