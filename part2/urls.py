"""
URL configuration for lab project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views

app_name = "part2"

urlpatterns = [
    path("course/<int:course_id>/", views.course_detail, name="course_detail"),
    path("add_project/", views.add_project, name="add_project"),
    path("projects/", views.project_list, name="project_list"),
    path("students/", views.StudentListView.as_view(), name="student_list"),
    path(
        "students/<int:pk>/", views.StudentDetailView.as_view(), name="student_detail"
    ),
    path("csv/", views.export_csv, name="export_csv"),
    path("pdf/", views.export_pdf, name="export_pdf"),
]
