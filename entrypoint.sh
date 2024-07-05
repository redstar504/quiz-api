#!/bin/bash

set -o errexit

export DJANGO_SETTINGS_MODULE=quiz.settings
python manage.py migrate

if [ "$ROLE" == "worker" ]; then
  echo "Starting worker..."
  celery -A quiz worker -l INFO
else
  echo "Starting server..."
  exec gunicorn -b 0.0.0.0 quiz.wsgi
fi