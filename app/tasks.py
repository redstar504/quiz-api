from celery import shared_task

from app.models import Topic


@shared_task
def generate_topic():
    topic = Topic(title="hooha", icon="fuzzy", color="black")
    topic.save()

    return topic.id
