import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'quiz.settings')
app = Celery('quiz')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f'Request: {self.request!r}')

# RENDER_REDIS_BACKEND_URL = os.environ.get('CELERY_BROKER_URL')
#
# if RENDER_REDIS_BACKEND_URL:
#     CELERY_BROKER_URL = RENDER_REDIS_BACKEND_URL
#     CELERY_RESULT_BACKEND = RENDER_REDIS_BACKEND_URL
# else:
#     CELERY_BROKER_URL = 'redis://localhost'
#     CELERY_RESULT_BACKEND = 'redis://localhost'
#
# celery_app = Celery('quiz')
#
# celery_app.conf.result_backend = CELERY_RESULT_BACKEND
