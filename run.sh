#!/usr/bin/env bash

gunicorn quiz.wsgi:application

#nohup python manage.py celery --production &