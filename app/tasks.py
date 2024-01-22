from celery import shared_task
from django.conf import settings
from app.models import Topic


@shared_task
def generate_topic(description):
    return settings.CELERY_BROKER_URL
