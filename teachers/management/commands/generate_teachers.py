from django.core.management.base import BaseCommand, CommandError
from teachers.models import Teacher


class Command(BaseCommand):
    help = "Add the specified number of teachers to  the database"

    def add_arguments(self, parser):
        parser.add_argument("number", type=int)

    def handle(self, *args, **options):
        for i in range(options["number"]):
            teachers_creation = Teacher(
                first_name=f"Teacher`s name: {i}",
                last_name=f"Teacher`s surname: {i}",
                subject=f"Subject: {i}"
            )
            teachers_creation.save()
            self.stdout.write(
                self.style.SUCCESS('Successfully added teacher "%s"' % teachers_creation)
            )
