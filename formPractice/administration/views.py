from django.shortcuts import render
from .forms import CreateStudentForm
from .models import Student
from django.http import HttpResponse


def create_student(request):
    form = CreateStudentForm()
    return render(request, 'administration/create_student.html', {'form': form})
