#!/usr/bin/python3

from __future__ import absolute_import
from django.conf import settings
import os
from celery import Celery
from celery.schedules import crontab


# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CatFacts.settings')
app = Celery('CatFacts')


CELERY_APP = Celery('CatFacts')
CELERY_APP.config_from_object('django.conf:settings')
CELERY_APP.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

CELERY_APP.conf.update(
	CELERY_RESULT_BACKEND = 'djcelery.backends.database:DatabaseBackend'
)


