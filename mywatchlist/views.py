from django.shortcuts import render
from mywatchlist.models import WatchlistItem
from django.http import HttpResponse
from django.core import serializers

def show_watchlist(request):
    data_watchlist = WatchlistItem.objects.all()
    context = {
    'data_watchlist': data_watchlist,
    'nama': 'Muhammad Fahreza Azka Arafat'
    }
    return render(request, "mywatchlist.html", context)
# Create your views here.

def show_xml(request):
    data = WatchlistItem.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = WatchlistItem.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

# Create your views here.
