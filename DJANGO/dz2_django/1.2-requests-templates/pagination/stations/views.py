from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
import csv
import os

def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    text = []
    with open('data-398-2018-08-30.csv') as f:
        DictReader_odj = csv.DictReader(f)
        for item in DictReader_odj:
            text.append(item)

        paginator = Paginator(text, 10)
        page_number = int(request.GET.get('page', 1))
        page = paginator.get_page(page_number)

    context = {
         'bus_stations':page.object_list,
         'page': page,
    }

    return render(request, 'stations/index.html', context)
