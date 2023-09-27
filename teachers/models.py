from django.db import models
from faker import Faker

fake = Faker()


class Teacher(models.Model):
    first_name = models.CharField(max_length=100, default=fake.first_name)
    last_name = models.CharField(max_length=100, default=fake.last_name)
    subject = models.CharField(max_length=50, default=fake.job)
