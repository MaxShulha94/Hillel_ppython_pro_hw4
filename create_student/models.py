from django.db import models
from faker import Faker

fake = Faker()


class Student(models.Model):
    first_name = models.CharField(max_length=100, default=fake.first_name)
    last_name = models.CharField(max_length=100, default=fake.last_name)
    birth_date = models.DateTimeField(default=fake.date_of_birth)

    def __str__(self):
        return f"Name: {self.first_name}, Surname: {self.last_name}, Date of birth: {self.birth_date};"
