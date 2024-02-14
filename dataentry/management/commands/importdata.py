from django.core.management.base import BaseCommand, CommandError
# from dataentry.models import Student
from django.apps import apps
import csv

# Proposed command -py manage.py importdata file_path model_name

class Command(BaseCommand):
    help = 'It will import data to the database from a csv file'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='Path of the csv file')
        parser.add_argument('model_name', type=str, help='Name of the model')

    def handle(self, *args, **kwargs):
        # write the logic
        file_path = kwargs['file_path']
        model_name = kwargs['model_name']

        # Search for the model across all installed apps
        model = None
        for app_config in apps.get_app_configs():
            # Try to search the model
            try:
                model = apps.get_model(app_config.label, model_name)
                break # stop searching once the model is found
            except LookupError:
                continue # model not found in this app, continue searching in next app.
        if not model:
            raise CommandError(f'Model "{model_name}" not found in this app!')
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                model.objects.create(**row)
        self.stdout.write(self.style.SUCCESS('Data imported from CSV file successfully!'))