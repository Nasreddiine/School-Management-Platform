from django.contrib import admin
from .models import Student, Professor, Course


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("student_id", "user", "class_level", "enrollment_date")
    search_fields = ("student_id", "user__username")

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "user":
            kwargs["queryset"] = db_field.related_model.objects.filter(role="student")
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    list_display = ("employee_id", "user", "department", "hire_date")
    search_fields = ("employee_id", "user__username")

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "user":
            kwargs["queryset"] = db_field.related_model.objects.filter(role="professor")
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("name", "professor")
    search_fields = ("name",)