from django.http import HttpResponse
from .models import Student
from faker import Faker

fake = Faker()


def generate_one(request):
    first_name = fake.first_name()
    last_name = fake.last_name()
    birth_date = fake.date_of_birth()
    student = Student(first_name=first_name, last_name=last_name, birth_date=birth_date)
    student.save()

    return HttpResponse(Student.__str__(student))


def generate_many(request):
    students = []
    generate_count = request.GET.get('count', 101)
    try:
        count = int(generate_count)
    except ValueError:
        return f'Please change value!'
    if 0 < count or 101 >= count:

        for _ in range(count):
            first_name = fake.first_name()
            last_name = fake.last_name()
            birth_date = fake.date_of_birth()
            student = Student(first_name=first_name, last_name=last_name, birth_date=birth_date)
            student.save()
            students.append(f'first_name: {first_name}, last_name: {last_name}, birth_date: {birth_date}; ')
        return HttpResponse(students)

    else:
        return HttpResponse('Count must be more than zero but less than one hundred!')