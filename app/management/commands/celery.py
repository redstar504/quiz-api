import shlex
import subprocess

from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument(
            "--production",
            action="store_true",
            dest="prod",
            help="Start celery in production mode"
        )

    def handle(self, *args, **options):
        if options['prod']:
            print("start celery prod")
            cmd = 'celery -A quiz worker --loglevel=info --concurrency=4'
            subprocess.Popen(shlex.split(cmd))
        else:
            print('Starting celery worker with autoreload...')
            cmd = 'watchmedo auto-restart --directory=./app --pattern=*.py --recursive -- celery -A quiz worker --loglevel=info'
            subprocess.call(shlex.split(cmd))

