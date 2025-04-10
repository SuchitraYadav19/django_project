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


def delete_emp(request, emp_id):
    print(emp_id)
    empl = Employee.objects.get(pk=emp_id)
    empl.delete()
    print(empl)

    return redirect("/employee/home/employee_service/")


def edit_emp(request, emp_id):
    print("edit employee with id: ", emp_id)
    empl = Employee.objects.get(pk=emp_id)
    return render(request, "employee_template/edit_employee.html", {'employees': empl})


def edit_employee_save(request, employee_id):

    if request.method == "POST":
        print("data is coming")
        emp_name = request.POST.get("InputName")
        # emp_id = request.POST.get("InputEmployeeID")
        emp_mail = request.POST.get("exampleInputEmail1")
        emp_pass = request.POST.get("exampleInputPassword1")
        emp_phone = request.POST.get("InputPhone")
        emp_address = request.POST.get("InputAddress")
        emp_depart = request.POST.get("InputDepartment")
        emp_is_active = request.POST.get("InputActiveCheck1")

        fetched_emp = Employee.objects.get(pk=employee_id)

        fetched_emp.name = emp_name
        fetched_emp.email = emp_mail
        # fetched_emp.id = emp_id
        fetched_emp.password = emp_pass
        fetched_emp.phone = emp_phone
        fetched_emp.address = emp_address
        fetched_emp.department = emp_depart
        if emp_is_active is None:
            fetched_emp.active = False
        else:
            fetched_emp.active = True
        fetched_emp.save()

    return redirect("/employee/home/employee_service/")
    # return render(request, "employee_template/.html", {'employees': fetched_emp})