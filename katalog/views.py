from django.shortcuts import render
from katalog.models import CatalogItem

# TODO: Create your views here.
def render_catalogue(request):
    return render(request, 'katalog.html', context)

data = CatalogItem.objects.all()
context = {
    'daftar_barang' : data,
    'Nama' : 'Muhammad Fahreza Azka Arafat',
    'NPM' : '2106752331'
}