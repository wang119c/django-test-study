from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def hello(request):
    return HttpResponse("hello")


def index(request):
    return render(request, 'index.html')


def home(request):
    return render(request, 'index.html')
