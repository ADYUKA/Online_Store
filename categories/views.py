from django.shortcuts import render
from django.http import HttpResponse
import datetime
from . import models


def LaptopListView(request):
    laptop_value = models.Laptop.objects.all()
    return render(request, 'laptop/laptop.html', {'laptop_key': laptop_value})


# def LaptopListView(request):
#     laptop_value = models.Laptop.objects.all()
#     html_file_name = 'laptop/laptop.html'
#     context = {
#         'laptop_key': laptop_value
#     }
#     return render(request, html_file_name, context)

def HelloView(request):
    return HttpResponse("<h1>Hello! It's my first project</h1>")


def NowDateView(request):
    now_date = datetime.datetime.now().replace(microsecond=0)
    return HttpResponse(f"<h1>Now date: {now_date} </h1>")


def ByeView(request):
    return HttpResponse("<h1>Goodbye my friend;)</h1>")