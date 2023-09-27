from django.urls import path

from . import views

urlpatterns = [
    path("generate-student/", views.generate_one, name="generate_one"),
    path("generate-students/", views.generate_many, name="generate_many"),
]
