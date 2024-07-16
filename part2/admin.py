from django.contrib import admin

# Register your models here.

from .models import Student, Course, Project


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email")
    search_fields = ("first_name", "last_name", "email")
    list_filter = ("first_name", "last_name", "email")


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
    search_fields = ("name",)
    filter_horizontal = ("students",)
    list_filter = ("name",)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("topic", "student", "languages_used", "duration")
    search_fields = (
        "topic",
        "student__first_name",
        "student__last_name",
        "languages_used",
    )
    list_filter = ("languages_used", "duration")
