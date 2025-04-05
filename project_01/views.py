from django.http import HttpResponse
from django.shortcuts import render
from .froms import UserForms
from datetime import datetime


def home_page(request):
    isactive = False
    if request.method == 'POST':
        value = request.POST.get('field1')
        print(value)
        if value is not None:
            isactive = True

    date = datetime.now()

    name = "Django project 01"
    list_of = ['One Piece', 'Naruto', 'Bleach', 'Gintama']
    mangaka = {'Oda':'One Piece', 'Kishimoto':'Naruto', 'Toriyama':'Dragon Ball'}

    data = {
        'date': date,
        'isactive': isactive,
        'name': name,
        'anime': list_of,
        'mangakas': mangaka
    }
    return render(request, "home.html", data)


def about_us(request):
    return render(request, "about_us.html")


def services(request):
    return render(request, "services.html")


def product_details(request, product_id):
    return HttpResponse(f"Welcome to product id: {product_id}")

