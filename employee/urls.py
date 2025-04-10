from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path('home/', employee_home),
    path('home/employee_service/', employee_service),
    path('home/employee_service/add_employee/', add_employee),
    path('home/employee_service/delete_employee/<int:emp_id>', delete_emp),
    path('home/employee_service/edit_employee/<int:emp_id>', edit_emp),
    path('home/employee_service/edit_employee_save/<int:emp_id>', edit_employee_save)
]