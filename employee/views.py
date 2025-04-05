from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def employee_home(request):
    return render(request, "employee_template/home_page.html")


def employee_service(request):
    return render(request, "employee_template/employee_service.html")

def add_employee(request):
    return render(request, "employee_template/add_employee.html")