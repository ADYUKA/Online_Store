from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
import datetime
from . import models


def laptop_detail_view(request, id):
    if request.method == 'GET':
        laptop = get_object_or_404(models.Laptop, id=id)
        contex_data = {
            'laptop': laptop
        }
        return render(request, 'laptop/laptop_detail.html', context=contex_data)


def laptop_list_view(request):
    if request.method == 'GET':
        laptop_value = models.Laptop.objects.all()
        context_data = {
            'laptop_key': laptop_value
        }
        return render(request, 'laptop/laptop.html', context=context_data)


def hello_view(request):
    if request.method == 'GET':
        return HttpResponse("<h1>Hello! It's my first project</h1>")


def now_date_view(request):
    if request.method == 'GET':
        now_date = datetime.datetime.now().replace(microsecond=0)
        return HttpResponse(f"<h1>Now date: {now_date} </h1>")


def bye_view(request):
    if request.method == 'GET':
        return HttpResponse("<h1>Goodbye my friend;)</h1>")