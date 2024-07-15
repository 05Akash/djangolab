from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

from .forms import StudentsForm
from .models import Students


def student(request):
    if request.method == "POST":
        form = StudentsForm(request.POST)
        if form.is_valid():
            student = form.save()
            return JsonResponse({"result": True})
        else:
            return JsonResponse({"result": False})
    else:
        form = StudentsForm()
    return render(request, "register_student.html", {"form": form})


def search(request):
    is_ajax = request.headers.get("X-Requested-with") == "XMLHttpRequest"
    if is_ajax:
        query = request.GET.get("query", "")
        students = Students.objects.filter(
            first_name__icontains=query
        ) | Students.objects.filter(last_name__icontains=query)
        results = []
        for student in students:
            student_data = {
                "id": student.id,
                "name": f"{student.first_name}{student.last_name}",
            }
            results.append(student_data)
        return JsonResponse({"results": results})
    else:
        return render(request, "search.html")
