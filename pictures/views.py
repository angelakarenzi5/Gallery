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


def search_results(request):

    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})
