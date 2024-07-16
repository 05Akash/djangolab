from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

from datetime import datetime, timedelta


def current_datetime(request):
    now = datetime.now()
    html = "<html><body>Current datetime: %s</body></html>" % now
    return HttpResponse(html)


def hours_4(request):
    ahead = datetime.now() + timedelta(hours=4)
    behind = datetime.now() - timedelta(hours=4)
    html = (
        "<html><body>Four hours behind datetime is %s. <br /> <br /> Four hours ahead datetime is %s.</body></html>"
        % (behind, ahead)
    )
    return HttpResponse(html)


def olul(request):
    context = {
        "fruits": ["Apple", "Banana", "jackfruit", "pineapple"],
        "students": ["Akash", "Praju", "Karthik", "Anubhav"],
    }
    return render(request, "olul.html", context)


def home(request):
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")
