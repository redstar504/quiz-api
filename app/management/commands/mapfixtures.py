from django.core.management import BaseCommand

from app.fixtures import map_quizzes


class Command(BaseCommand):
    help = 'Maps the raw.json file provided by FM to loadable fixture data'

    def add_arguments(self, parser):
        parser.add_argument("--model", type=str)

    def handle(self, *args, **options):
        model = options["model"]
        if model == 'quizzes':
            map_quizzes.run_mapping()

        self.stdout.write(self.style.SUCCESS('Successfully mapped data'))
