from time import sleep

from celery import Celery

app = Celery('celery_test', broker='redis://localhost')


@app.task
def test_task():
    print("Task started")
    sleep(10)
    print("Task completed")


if __name__ == '__main__':
    app.worker_main(['worker', '-l', 'info'])
