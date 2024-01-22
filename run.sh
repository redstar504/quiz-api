#!/usr/bin/env bash

set -o errexit

gunicorn quiz.wsgi:application &
echo "waiting 10 seconds before starting celery..."

sleep 10

python manage.py celery --production &