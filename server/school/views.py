from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from accounts.permissions import IsAdmin, IsProfessor, IsStudent
from .models import Student, Professor, Course
from .serializers import StudentSerializer, CourseSerializer


class AdminStudentsView(APIView):
    permission_classes = [IsAdmin]

    def get(self, request):
        students = Student.objects.select_related("user").all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)


class ProfessorCoursesView(APIView):
    permission_classes = [IsProfessor]

    def get(self, request):
        try:
            professor = request.user.professor_profile
        except Professor.DoesNotExist:
            return Response(
                {"detail": "No professor profile linked to this account."},
                status=status.HTTP_404_NOT_FOUND,
            )

        courses = Course.objects.filter(professor=professor).select_related("professor__user")
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)


class StudentCoursesView(APIView):
    permission_classes = [IsStudent]

    def get(self, request):
        try:
            student = request.user.student_profile
        except Student.DoesNotExist:
            return Response(
                {"detail": "No student profile linked to this account."},
                status=status.HTTP_404_NOT_FOUND,
            )

        # No enrollment model yet — returns empty list for now
        return Response([])