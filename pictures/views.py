from django.shortcuts import render, redirect 
from django.http import HttpResponse, Http404
from datetime as dt 
from .models import Image


def pictures_of_day(request):
    date = dt.date.today()
    return render(request, 'today-pictures.html', {"date": date,})
