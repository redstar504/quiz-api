#!/bin/bash

set -o errexit

export DJANGO_SETTINGS_MODULE=quiz.settings
python manage.py migrate
exec gunicorn -b 0.0.0.0 quiz.wsgi