from django.shortcuts import render
from django.http import HttpResponse
import datetime


def HelloView(request):
    return HttpResponse("<h1>Hello! It's my first project</h1>")


def NowDateView(request):
    now_date = datetime.datetime.now().replace(microsecond=0)
    return HttpResponse(f"<h1>Now date: {now_date} </h1>")


def ByeView(request):
    return HttpResponse("<h1>Goodbye my friend;)</h1>")