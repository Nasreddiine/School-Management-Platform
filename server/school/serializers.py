from rest_framework import serializers
from .models import Student, Professor, Course


class StudentSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source="user.username", read_only=True)
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = Student
        fields = [
            "id",
            "username",
            "full_name",
            "student_id",
            "birth_date",
            "class_level",
            "enrollment_date",
        ]

    def get_full_name(self, obj):
        return f"{obj.user.first_name} {obj.user.last_name}".strip() or obj.user.username


class ProfessorSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source="user.username", read_only=True)
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = Professor
        fields = [
            "id",
            "username",
            "full_name",
            "employee_id",
            "department",
            "hire_date",
        ]

    def get_full_name(self, obj):
        return f"{obj.user.first_name} {obj.user.last_name}".strip() or obj.user.username


class CourseSerializer(serializers.ModelSerializer):
    professor_name = serializers.CharField(source="professor.user.username", read_only=True)

    class Meta:
        model = Course
        fields = [
            "id",
            "name",
            "description",
            "professor",
            "professor_name",
        ]