# TODO: Implement Routings Here
from django.urls import path
from katalog.views import render_catalogue

app_name = 'katalog'

urlpatterns = [path('', render_catalogue, name='render_catalogue')]