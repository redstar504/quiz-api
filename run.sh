#!/usr/bin/env bash

set -o errexit

#gunicorn quiz.wsgi:application &

nohup python manage.py celery --production &