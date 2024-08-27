import os
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

LOG_PATH = os.path.abspath(os.path.join(BASE_DIR, "../logs"))

DEFAULT_LOG = "djtodos.log"
DJANGO_FILE = "django.log"
CELERY_FILE = "celery.log"

DEFAULT_FILE_PATH = os.path.abspath(os.path.join(LOG_PATH, DEFAULT_LOG))
DJANGO_FILE_PATH = os.path.abspath(os.path.join(LOG_PATH, DJANGO_FILE))
CELERY_FILE_PATH = os.path.abspath(os.path.join(LOG_PATH, CELERY_FILE))

if not os.path.exists(LOG_PATH):
    os.makedirs(LOG_PATH)

FILE_LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "detailed": {
            "format": "[%(asctime)s] %(levelname)s [%(name)s %(pathname)s:%(lineno)s - %(funcName)s() ] %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S %Z",
        },
        "simple": {
            "format": "{levelname} {message}",
            "style": "{",
        },
    },
    "handlers": {
        "file": {
            "level": "DEBUG",
            "class": "logging.FileHandler",
            "formatter": "detailed",
            "filename": DEFAULT_FILE_PATH,
        },
        "django_file": {
            "level": "DEBUG",
            "class": "logging.FileHandler",
            "formatter": "detailed",
            "filename": DJANGO_FILE_PATH,
        },
        "celery_file": {
            "level": "DEBUG",
            "class": "logging.FileHandler",
            "formatter": "detailed",
            "filename": CELERY_FILE_PATH,
        },
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "simple",
        },
    },
    "loggers": {
        "": {
            "handlers": ["file"],
            "level": "DEBUG",
            "propagate": True,
        },
        "django.db.backends": {
            "handlers": ["django_file"],
            "level": "DEBUG",
            
            "propagate": False,
        },
        "CELERY_WORKER": {
            "handlers": ["file"],
            "level": "INFO",
            "propagate": True,
        },
    },
}