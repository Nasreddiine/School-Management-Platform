from rest_framework.permissions import BasePermission


class IsAdmin(BasePermission):
    message = "Only administrators can access this."

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.role == "admin"
        )


class IsProfessor(BasePermission):
    message = "Only professors can access this."

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.role == "professor"
        )


class IsStudent(BasePermission):
    message = "Only students can access this."

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.role == "student"
        )