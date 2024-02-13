from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Greets the user'

    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help='Name of the person to greet')

    def handle(self, *args, **kwargs):
        # write the logic
        name = kwargs['name']
        greeting = f'Hi {name}, Good morning!'
        self.stdout.write(self.style.SUCCESS(greeting))