from django.core.management.base import BaseCommand
from dataentry.models import Student

class Command(BaseCommand):
    help = 'It will insert data to the database'

    def handle (self, *args, **kwargs):
        # write the logic
        # create new a student
        dataset = [
            {'roll_no': 1002, 'name': 'Alric', 'age': 21},
            {'roll_no': 1005, 'name': 'Robin', 'age': 24},
            {'roll_no': 1006, 'name': 'Tina', 'age': 23},
        ]

        for data in dataset:
            roll_no = data['roll_no']
            existing_record = Student.objects.filter(roll_no=roll_no)
            if not existing_record:
                Student.objects.create(**data)
            else:
                self.stdout.write(self.style.WARNING(f'Student with roll_no {roll_no} already exists'))
        self.stdout.write(self.style.SUCCESS('Successfully inserted data'))

