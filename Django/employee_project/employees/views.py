from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Employee

def home(request):
    return render(request, "employees/home.html")


def employees(request):
    data = Employee.objects.all()
    return HttpResponse(data)