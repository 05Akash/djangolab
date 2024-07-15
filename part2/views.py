from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.template.loader import get_template
from django.views.generic import ListView, DetailView

# Create your views here.

from .models import Course, Project, Student
from .forms import ProjectForm
import csv
from xhtml2pdf import pisa


def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    students = course.students.all()
    return render(
        request,
        "course_details.html",
        {"course": course, "students": students},
    )


def add_project(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("part2:project_list")
    else:
        form = ProjectForm()
    return render(request, "add_project.html", {"form": form})


def project_list(request):
    projects = Project.objects.all()
    return render(request, "project_list.html", {"projects": projects})


class StudentListView(ListView):
    model = Student
    template_name = "student_list.html"
    context_object_name = "students"


class StudentDetailView(DetailView):
    model = Student
    template_name = "student_detail.html"
    context_object_name = "student"


def export_csv(request):
    response = HttpResponse(
        content_type="text/csv",
        headers={"Content-Disposition": 'attachment; filename="student_details.csv"'},
    )

    writer = csv.writer(response)
    writer.writerow(["ID", "First Name", "Last Name", "Email"])

    students = Student.objects.all()
    for student in students:
        writer.writerow(
            [student.id, student.first_name, student.last_name, student.email]
        )

    return response


def export_pdf(request):
    response = HttpResponse(
        content_type="text/pdf",
        headers={"Content-Disposition": 'attachment; filename="student_details.pdf"'},
    )
    students = Student.objects.all()
    context = {"students": students}

    template = get_template("student_details.html")
    html = template.render(context)

    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
        return HttpResponse("Error generating PDF<pre>" + html + "</pre>")
    return response
