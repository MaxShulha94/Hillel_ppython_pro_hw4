from django.http import HttpResponse
from faker import Faker

from .models import Student

fake = Faker()


def generate_one(request):
    first_name = fake.first_name()
    last_name = fake.last_name()
    birth_date = fake.date_of_birth()
    student = Student(first_name=first_name, last_name=last_name, birth_date=birth_date)
    student.save()

    return HttpResponse(str(student))


def generate_many(request):
    students = []
    generate_count = request.GET.get("count", 100)
    try:
        count = int(generate_count)
    except ValueError:
        return f"Please change value!"
    if count <= 0 or 101 <= count:
        return HttpResponse("Count must be more than zero but less than one hundred!")
    else:
        for _ in range(count):
            first_name = fake.first_name()
            last_name = fake.last_name()
            birth_date = fake.date_of_birth()
            student = Student(
                first_name=first_name, last_name=last_name, birth_date=birth_date
            )
            student.save()
            students.append(
                f"first_name: {first_name}, last_name: {last_name}, birth_date: {birth_date} "
            )
        return HttpResponse(students)
