from django.urls import path
from .views import AdminStudentsView, ProfessorCoursesView, StudentCoursesView

urlpatterns = [
    path("admin/students/", AdminStudentsView.as_view(), name="admin-students"),
    path("professor/courses/", ProfessorCoursesView.as_view(), name="professor-courses"),
    path("student/courses/", StudentCoursesView.as_view(), name="student-courses"),
]