from django.shortcuts import render


def index(request):
    name = "project"
    return render(request, "base.html", {"name": name})

