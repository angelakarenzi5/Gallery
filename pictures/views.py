from django.shortcuts import render, redirect 
from django.http import HttpResponse, Http404
import datetime as dt 
from .models import Image


def pictures_of_day(request):
    date = dt.date.today()
    pictures = Image.objects.all()

    return render(request, 'today-pictures.html', {"date": date,"pictures":pictures})

def pictures(request,pictures_id):
    try:
        picture = Picture.objects.get(id = picture_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"/picture.html", {"picture":picture})
