from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return HttpResponse("<h1>welcome to django developement</h1>")

def product(request):
    return HttpResponse("<h1>this is product page</h1>")

def orders(request):
    return HttpResponse("<h1>this is order page</h1>")

def customers(request):
    return HttpResponse("<h1>this is customers page</h1>")