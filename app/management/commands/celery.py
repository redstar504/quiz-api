import shlex
import subprocess

from django.core.management.base import BaseCommand

class Command(BaseCommand):
    def handle(self, *args, **options):
        cmd = 'watchmedo auto-restart --directory=./app --pattern=*.py --recursive -- celery -A quiz worker --loglevel=info'
        print('Starting celery worker with autoreload...')
        subprocess.call(shlex.split(cmd))
