from celery import shared_task
from django.conf import settings
from app.models import Topic


@shared_task
def generate_topic(description):
    print(settings.CELERY_BROKER_URL)
    # topic = Topic(title="hooha", icon="fuzzy", color="black")
    # topic.save()
    #
    # return topic.id
