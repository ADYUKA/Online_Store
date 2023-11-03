from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
import datetime
from . import models
from .forms import CreateLaptopForm
from .models import Laptop


def laptop_detail_view(request, id):
    if request.method == 'GET':
        laptop = get_object_or_404(models.Laptop, id=id)
        contex_data = {
            'laptop': laptop,
        }
        return render(request, 'laptop/laptop_detail.html', context=contex_data)


def laptop_list_view(request):
    if request.method == 'GET':
        laptop_value = models.Laptop.objects.all()
        context_data = {
            'laptop_key': laptop_value,
            'user': request.user
        }
        return render(request, 'laptop/laptop.html', context=context_data)


def laptop_create_view(request):
    if request.method == 'GET':
        context_data = {
            'form': CreateLaptopForm
        }

        return render(request, 'laptop/create.html', context=context_data)

    if request.method == 'POST':
        data, files = request.POST, request.FILES
        form = CreateLaptopForm(data, files)

        if form.is_valid():
            cleaned_data = form.cleaned_data
            Laptop.objects.create(
                image=cleaned_data.get('image'),
                model=cleaned_data.get('model'),
                cost=cleaned_data.get('cost'),
                description=cleaned_data.get('description'),
                condition=cleaned_data.get('condition'),
                laptop_types=cleaned_data.get('laptop_types'),
                release_year=cleaned_data.get('release_year'),
            )
            return redirect('/laptop/')

        return render(request, '/laptop/create.html', context={'form': form})


def now_date_view(request):
    if request.method == 'GET':
        now_date = datetime.datetime.now().replace(microsecond=0)
        return HttpResponse(f"<h1>Now date: {now_date} </h1>")




