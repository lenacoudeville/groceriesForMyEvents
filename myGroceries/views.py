from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("<H1>Bienvenue sur GroceriesForMyEvents</H1>")