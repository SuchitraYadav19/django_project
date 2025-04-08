from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
from .models import Employee


def employee_home(request):
    return render(request, "employee_template/home_page.html")


def employee_service(request):
    employees = Employee.objects.all()
    return render(request, "employee_template/employee_service.html",{'employees':employees})


def add_employee(request):
    if request.method == "POST":
        print("data is coming")
        emp_name = request.POST.get("InputName")
        emp_id = request.POST.get("InputEmployeeID")
        emp_mail = request.POST.get("exampleInputEmail1")
        emp_pass = request.POST.get("exampleInputPassword1")
        emp_phone = request.POST.get("InputPhone")
        emp_address = request.POST.get("InputAddress")
        emp_depart = request.POST.get("InputDepartment")
        emp_is_active = request.POST.get("InputActiveCheck1")

        emp_obj = Employee()
        emp_obj.name = emp_name
        emp_obj.employee_id = emp_id
        emp_obj.email = emp_mail
        emp_obj.password = emp_pass
        emp_obj.phone = emp_phone
        emp_obj.address = emp_address
        emp_obj.department = emp_depart
        if emp_is_active is None:
            emp_obj.active = False
        else:
            emp_obj.active = True

        emp_obj.save()

        return redirect("/employee/home/employee_service/")

    return render(request, "employee_template/add_employee.html")