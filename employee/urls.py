from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path('home/', employee_home),
    path('home/employee_service/', employee_service),
    path('home/employee_service/add_employee/', add_employee)
]