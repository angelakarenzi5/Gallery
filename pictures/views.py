from django.shortcuts import render, redirect 
from django.http import HttpResponse, Http404
import datetime as dt 
from .models import Image, Location 


def pictures_of_day(request):
    date = dt.date.today()
    pictures = Image.objects.all()

    return render(request, 'today-pictures.html', {"date": date,"images":pictures})

def image(request,image_id):
    try:
        image = Image.objects.get(id = image_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"/image.html", {"image":image})


def search_results(request):

    if 'category' in request.GET and request.GET["category"]:
        search_term = request.GET.get("category")
        searched_images = Image.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})

def location (request, location_id):
    location = Location.objects.get(id = location_id)
    images = Image.objects.filter(location = location.id)
    return render(request,'location.html', {"images":images, "location":location})