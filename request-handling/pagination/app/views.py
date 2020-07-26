from django.shortcuts import render_to_response, redirect
from django.core.paginator import Paginator
from django.urls import reverse
from django.conf import settings

from urllib import parse
from csv import DictReader

bus_stations_list = None

with open(settings.BUS_STATION_CSV, 'r') as csvfile:
    bus_stations_list = list(DictReader(csvfile))


def index(request):
    return redirect(reverse(bus_stations))


def bus_stations(request):
    by_page = 10
    current_page = int(request.GET.get('page', 1))
    next_page_url = f'{reverse("bus_stations")}?{parse.urlencode({"page": current_page + 1})}'
    prev_page_url = f'{reverse("bus_stations")}?{parse.urlencode({"page": current_page - 1})}'

    paginator = Paginator(bus_stations_list, by_page)
    page_obj = paginator.get_page(current_page)
    content = page_obj.object_list

    print(prev_page_url)
    print(next_page_url)

    return render_to_response('index.html', context={
        'bus_stations': content,
        'current_page': current_page,
        'prev_page_url': prev_page_url if page_obj.has_previous() else None,
        'next_page_url': next_page_url if page_obj.has_next() else None,
    })

