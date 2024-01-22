#!/usr/bin/env bash
# exit on error
set -o errexit

poetry install

python manage.py collectstatic --no-input
python manage.py migrate

nohup celery -A quiz worker --concurrency=4 --loglevel=debug --logfile=celery.log > celery.out 2>&1 &