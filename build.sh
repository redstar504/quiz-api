#!/usr/bin/env bash
# exit on error
set -o errexit

poetry install

python manage.py collectstatic --no-input
python manage.py migrate

#DJANGO_SETTINGS_MODULE=quiz.settings celery -A quiz.settings worker --loglevel=info &