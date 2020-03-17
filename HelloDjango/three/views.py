from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template import loader


def index(request):
    three_index = loader.get_template('three.html')
    result = three_index.render()
    return HttpResponse(result)
