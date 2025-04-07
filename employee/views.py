from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.


def employee_home(request):
    return render(request, "employee_template/home_page.html")


def employee_service(request):
    return render(request, "employee_template/employee_service.html")


def add_employee(request):
    if request.method == "POST":
        print("data is coming")
        return redirect("/employee/home/employee_service/")

    return render(request, "employee_template/add_employee.html")