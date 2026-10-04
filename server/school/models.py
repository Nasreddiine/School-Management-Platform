from django.conf import settings
from django.db import models


class Student(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="student_profile",
    )
    student_id = models.CharField(max_length=20, unique=True)
    birth_date = models.DateField(null=True, blank=True)
    class_level = models.CharField(max_length=50, blank=True)
    enrollment_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} ({self.student_id})"


class Professor(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="professor_profile",
    )
    employee_id = models.CharField(max_length=20, unique=True)
    department = models.CharField(max_length=100, blank=True)
    hire_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} ({self.employee_id})"


class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    professor = models.ForeignKey(
        Professor,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="courses",
    )

    def __str__(self):
        return self.name