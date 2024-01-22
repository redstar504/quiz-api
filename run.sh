#!/usr/bin/env bash

gunicorn quiz.wsgi:application &

sleep 10

echo "start celery"

celery -qA quiz worker --loglevel=fatal &

#nohup python manage.py celery --production &