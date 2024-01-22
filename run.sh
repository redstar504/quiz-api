#!/usr/bin/env bash

set -o errexit

gunicorn quiz.wsgi:application &

exit 0

#nohup python manage.py celery --production &