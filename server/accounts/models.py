from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = "admin", "Admin"
        PROFESSOR = "professor", "Professor"
        STUDENT = "student", "Student"

    role = models.CharField(max_length=20, choices=Role.choices)